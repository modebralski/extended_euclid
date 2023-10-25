def main():
    a_value = 75
    b_value = 28
    extended_euclid_step(a_value, b_value)


def extended_euclid_step(a_val: int, b_val: int, t0_val: int = 0, t_val: int = 1, first_step: bool = True):
    q_val = int(a_val / b_val)
    r_val = a_val % b_val
    if first_step == False:
        t_val = t0_val - q_val * t_val
    print(f"a: {a_val} b: {b_val} r: {r_val} t0: {t0_val} t: {t_val} q: {q_val}")
    return [a_val, b_val, r_val, t0_val, t_val, q_val]


if __name__ == "__main__":
    main()
