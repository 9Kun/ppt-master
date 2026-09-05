import json
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]


def simple(effect="entrance_fade", trigger="on-click", order=1, duration=0.2, delay=0.0):
    row = {"effect": effect, "trigger": trigger, "order": order, "duration": duration}
    if delay:
        row["delay"] = delay
    return row


def automatic(effect="entrance_fade", order=1, duration=0.16, delay=0.04):
    return simple(
        effect=effect,
        trigger="after-previous",
        order=order,
        duration=duration,
        delay=delay,
    )


def interactive(effect, order, trigger_shape, delay=0.0, duration=0.08, direction=None):
    row = {
        "effect": effect,
        "trigger": "on-click",
        "trigger_shape": trigger_shape,
        "order": order,
        "delay": round(delay, 2),
        "duration": duration,
        "restart": "always",
    }
    if direction:
        row["effect_options"] = {"direction": direction}
    return row


def add(groups, group_id, row):
    block = groups.setdefault(group_id, {})
    block.setdefault("effects", []).append(row)


def retime_drawing(groups, trigger_shape, ordered_groups, order_start):
    """Reorder one existing console drawing without changing its total span."""
    delay = 0.18
    for offset, group_id in enumerate(ordered_groups):
        row = next(
            effect
            for effect in groups[group_id]["effects"]
            if effect.get("trigger_shape") == trigger_shape
        )
        row["order"] = order_start + offset
        row["delay"] = round(delay, 2)
        delay += 0.18 if row["effect"] == "entrance_appear" else 0.42


def reveal_slide(pairs):
    groups = {}
    for order, (answer, explain) in enumerate(pairs, 1):
        groups[answer] = simple(order=order)
        if explain:
            groups[explain] = simple(trigger="with-previous", order=order, duration=0.3)
    return {"groups": groups}


def console_slide(task1_shapes, task2_shapes, task1_terms, task2_terms, fills1=(), fills2=()):
    groups = {}
    # Run task 1: status → drawing → fill → typewriter → completion.
    run1 = "run-t1-hit"
    add(groups, "terminal-guide-initial", interactive("exit_appear", 1, run1))
    add(groups, "terminal-guide-active", interactive("exit_appear", 2, run1))
    add(groups, "terminal-running", interactive("entrance_appear", 3, run1))
    delay = 0.18
    directions = ("right", "down", "left", "up")
    for index, shape in enumerate(task1_shapes):
        add(groups, shape, interactive("entrance_wipe", 10 + index, run1, delay, 0.36, directions[index % 4]))
        delay += 0.42
    for index, shape in enumerate(fills1):
        add(groups, shape, interactive("entrance_appear", 30 + index, run1, delay, 0.12))
        delay += 0.18
    for index, char in enumerate(task1_terms):
        add(groups, char, interactive("entrance_wipe", 40 + index, run1, delay + index * 0.1, 0.08, "right"))
    done_delay = delay + len(task1_terms) * 0.1 + 0.18
    add(groups, "done-t1", interactive("entrance_appear", 90, run1, done_delay, 0.1))
    add(groups, "terminal-running", interactive("exit_appear", 91, run1, done_delay, 0.05))

    # Run task 2 with the same WPS-friendly chain.
    run2 = "run-t2-hit"
    add(groups, "terminal-guide-initial", interactive("exit_appear", 201, run2))
    add(groups, "terminal-guide-active", interactive("exit_appear", 202, run2))
    add(groups, "terminal-running", interactive("entrance_appear", 203, run2))
    delay = 0.18
    for index, shape in enumerate(task2_shapes):
        add(groups, shape, interactive("entrance_wipe", 210 + index, run2, delay, 0.36, directions[index % 4]))
        delay += 0.42
    for index, shape in enumerate(fills2):
        add(groups, shape, interactive("entrance_appear", 230 + index, run2, delay, 0.12))
        delay += 0.18
    for index, char in enumerate(task2_terms):
        add(groups, char, interactive("entrance_wipe", 240 + index, run2, delay + index * 0.1, 0.08, "right"))
    done_delay = delay + len(task2_terms) * 0.1 + 0.18
    add(groups, "done-t2", interactive("entrance_appear", 290, run2, done_delay, 0.1))
    add(groups, "terminal-running", interactive("exit_appear", 291, run2, done_delay, 0.05))

    # Task 2 selection. run-t1-hit exits first so it is available on slide entry.
    select2 = "task-t2-hit"
    add(groups, "run-t1-hit", interactive("exit_appear", 301, select2))
    for group_id in ("code-t1-initial", "run-t1-initial", "terminal-guide-initial"):
        add(groups, group_id, interactive("exit_appear", 302, select2))
    add(groups, "code-t2-state", interactive("entrance_appear", 310, select2, 0.06))
    add(groups, "run-t2-button", interactive("entrance_appear", 311, select2, 0.06))
    add(groups, "run-t2-hit", interactive("entrance_appear", 312, select2, 0.06))
    add(groups, "terminal-guide-active", interactive("entrance_appear", 313, select2, 0.1))

    # Task 1 selection and cross-task cleanup.
    select1 = "task-t1-hit"
    for group_id in ("code-t1-initial", "run-t1-initial", "terminal-guide-initial"):
        add(groups, group_id, interactive("exit_appear", 401, select1))
    add(groups, "code-t1-state", interactive("entrance_appear", 410, select1, 0.06))
    add(groups, "run-t1-button", interactive("entrance_appear", 411, select1, 0.06))
    add(groups, "run-t1-hit", interactive("entrance_appear", 412, select1, 0.06))
    add(groups, "terminal-guide-active", interactive("entrance_appear", 413, select1, 0.1))

    # Switching tasks resets code, buttons, status, drawing, output, and completion.
    for group_id in ("code-t1-state", "run-t1-button", "done-t1", *task1_shapes, *fills1, *task1_terms):
        add(groups, group_id, interactive("exit_appear", 500, select2))
    for group_id in ("code-t2-state", "run-t2-button", "run-t2-hit", "done-t2", *task2_shapes, *fills2, *task2_terms):
        add(groups, group_id, interactive("exit_appear", 600, select1))

    return {"interactive_sequence_mode": "wps", "groups": groups}


slides = {
    "01_封面_多彩画笔大师": {
        "groups": {
            "badge-stage": automatic(order=1, duration=0.22),
            "paint-trail": automatic(order=2, duration=0.2, delay=0.06),
        }
    },
    "02_两小时彩色探险航线": {
        "groups": {
            "route-spine": automatic(order=1, duration=0.18),
            "stage-review": automatic(order=2),
            "stage-learn": automatic(order=3),
            "stage-choice": automatic(order=4),
            "stage-project": automatic(order=5),
        }
    },
    "03_第4课知识抢答_1-5": reveal_slide([(f"answer-{n}", None) for n in range(1, 6)]),
    "04_第4课知识抢答_6-10": reveal_slide([(f"answer-{n}", None) for n in range(6, 11)]),
    "07_填充三明治": {
        "groups": {
            "sandwich-stack": automatic(order=1),
            "technical-fact": automatic(order=2),
            "code-example": automatic(order=3),
            "error-tip": automatic(order=4),
        }
    },
    "12_选择闯关_1-2": reveal_slide([("answer-1-correct", "answer-1-explain"), ("answer-2-correct", "answer-2-explain")]),
    "13_选择闯关_3-4": reveal_slide([("answer-3-correct", "answer-3-explain"), ("answer-4-correct", "answer-4-explain")]),
    "14_选择闯关_5-6": reveal_slide([("answer-5-correct", "answer-5-explain"), ("answer-6-correct", "answer-6-explain")]),
    "15_选择闯关_7-8": reveal_slide([("answer-7-correct", "answer-7-explain"), ("answer-8-correct", "answer-8-explain")]),
    "22_易错警示_海龟修理站": reveal_slide([(f"answer-{n}", None) for n in range(1, 5)]),
    "23_作品验收_彩色徽章发布会": {
        "groups": {
            "acceptance-list": automatic(order=1),
            "showcase-script": automatic(order=2),
            "home-action": automatic(order=3),
        }
    },
}

# Ordinary teaching pages enter automatically after the page turn. Quiz/reveal
# pages and code demonstration/challenge pages stay presenter-controlled or
# static so a click cannot accidentally skip an answer or run state.
for stem in (
    "05_项目启动_海龟岛彩色徽章",
    "06_三位颜色管理员",
    "08_背景和画笔粗细",
    "09_circle的两个数字",
    "16_课间休息",
):
    slides[stem] = {
        "animation": {
            "effect": "entrance_fade",
            "trigger": "after-previous",
            "duration": 0.16,
            "stagger": 0.06,
        }
    }

slides["04_第4课知识抢答_6-10"]["groups"]["quiz-champion"] = simple(order=6, duration=0.3)
slides["22_易错警示_海龟修理站"]["groups"]["repair-rhyme"] = simple(order=5, duration=0.3)

circle1 = [f"canvas-t1-seg-{n:02d}" for n in range(1, 5)]
circle2 = [f"canvas-t2-seg-{n:02d}" for n in range(1, 5)]
term1 = [f"term-t1-c{n:02d}" for n in range(1, 9)]
term2 = [f"term-t2-c{n:02d}" for n in range(1, 9)]
slides["11_控制台_彩色圆实验站"] = console_slide(circle1, circle2, term1, term2)

square1 = [f"canvas-t1-seg-{n:02d}" for n in range(1, 5)]
square2 = [f"canvas-t2-seg-{n:02d}" for n in range(1, 5)]
slides["18_控制台_填充正方形实验站"] = console_slide(
    square1, square2, term1, term2, ("canvas-t1-fill",), ("canvas-t2-fill",)
)

badge1 = [f"canvas-t1-outer-{n:02d}" for n in range(1, 5)] + [f"canvas-t1-inner-{n:02d}" for n in range(1, 5)]
badge2 = [f"canvas-t2-outer-{n:02d}" for n in range(1, 5)] + [f"canvas-t2-inner-{n:02d}" for n in range(1, 5)]
badge_term1 = [f"term-t1-l{line}-c{char:02d}" for line in (1, 2) for char in range(1, 5)]
badge_term2 = [f"term-t2-l{line}-c{char:02d}" for line in (1, 2) for char in range(1, 5)]
slides["20_控制台_海龟岛徽章工坊"] = console_slide(
    badge1,
    badge2,
    badge_term1,
    badge_term2,
    ("canvas-t1-outer-fill", "canvas-t1-inner-fill"),
    ("canvas-t2-outer-fill", "canvas-t2-inner-fill"),
)

badge_groups = slides["20_控制台_海龟岛徽章工坊"]["groups"]
retime_drawing(
    badge_groups,
    "run-t1-hit",
    [
        *[f"canvas-t1-outer-{n:02d}" for n in range(1, 5)],
        "canvas-t1-outer-fill",
        *[f"canvas-t1-inner-{n:02d}" for n in range(1, 5)],
        "canvas-t1-inner-fill",
    ],
    10,
)
retime_drawing(
    badge_groups,
    "run-t2-hit",
    [
        *[f"canvas-t2-outer-{n:02d}" for n in range(1, 5)],
        "canvas-t2-outer-fill",
        *[f"canvas-t2-inner-{n:02d}" for n in range(1, 5)],
        "canvas-t2-inner-fill",
    ],
    210,
)

payload = {"version": 1, "slides": slides}
(PROJECT / "animations.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {PROJECT / 'animations.json'}")
