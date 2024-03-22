import numpy


def dijkstra():
    print("starting dijkstra...")
    w = {
        "s": {"a": 5, "b": 3, "c": 2, "d": 4},
        "a": {"e": 3},
        "b": {"a": 2, "f": 1},
        "c": {"f": 4, "h": 8},
        "d": {"c": 1, "h": 6},
        "e": {"g": 1},
        "f": {"e": 1, "h": 2},
        "h": {"g": 4},
    }

    mw = {}
    mw = {
        "a": 100,
        "b": 100,
        "c": 100,
        "d": 100,
        "e": 100,
        "f": 100,
        "g": 100,
        "h": 100,
    }
    mw["a"] = w["s"]["a"]
    mw["b"] = w["s"]["b"]
    mw["c"] = w["s"]["c"]
    mw["d"] = w["s"]["d"]

    finished_mw = {}

    while len(mw) > 0:
        min_k, min_v = choose_min_val(mw, finished_mw)
        print(min_k, "-", min_v)
        # 从mw中移除元素
        finished_mw[min_k] = min_v
        # 将最新直接可达的元素放入mw
        if min_k in w:
            for k, _ in w[min_k].items():
                if k not in finished_mw.keys() and mw[min_k] + w[min_k][k] < mw[k]:
                    mw[k] = mw[min_k] + w[min_k][k]
        del mw[min_k]

    print("finished_mw=", finished_mw)


def choose_min_val(mw, finished_mw):
    min_val = 100
    min_key = ""
    for k, v in mw.items():
        if k in finished_mw.keys():
            continue
        if v < min_val:
            min_val = v
            min_key = k
    return min_key, min_val


if __name__ == "__main__":
    print("starting...")
    dijkstra()