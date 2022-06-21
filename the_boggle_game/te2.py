def main():
    let = ['10', '2', '3']
    x = sorted(let, key=lambda ele: int(ele))
    print(x)


if __name__ == '__main__':
    main()

