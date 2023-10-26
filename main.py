def main():
    a_value, mod_value = 61, 61
    b_value = 17
    while True:
        a_value, b_value, t0_value, t_value, q_value, r_value = extended_euclid_step(mod_value, a_value, b_value)
        if r_value != 0:
            a_value, b_value, t0_value, t_value, q_value, r_value = extended_euclid_step(mod_val=mod_value, a_val=a_value,
                                                                                         b_val=b_value, q_val=q_value,
                                                                                         t0_val=t0_value, t_val=t_value,
                                                                                         first_step=False)
        else:
            return False


def extended_euclid_step(mod_val, a_val, b_val, q_val=0, t0_val=0, t_val=1, first_step=True):
    r_value = a_val % b_val
    q_value = int(a_val / b_val)
    if not first_step:
        t0_value = t_val
        t_value = (t0_val - q_val * t_val) % mod_val
    else:
        t_value = t_val
        t0_value = t0_val
    print(f"a: {a_val} b: {b_val}, r: {r_value} t0: {t0_value} t: {t_value} q: {q_value}")
    return [b_val, r_value, t0_value, t_value, q_value, r_value]


if __name__ == "__main__":
    main()
