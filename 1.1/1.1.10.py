def print_pattern():
    # Define the pattern as a list of strings
    pattern = [
        "                ********",
        "               ************",
        "               ####....#.",
        "             #..###.....##....",
        "             ###.......######              ###                 ###           ###           ###",
        "                ...........               #...#               #...#         #...#         #...#",
        "               ##*#######                 #.#.#               #.#.#         #.#.#         #.#.#",
        "            ####*******######             #.#.#               #.#.#         #.#.#         #.#.#",
        "           ...#***.****.*###....          #...#               #...#         #...#         #...#",
        "           ....**********##.....           ###                 ###           ###           ###",
        "           ....****    *****....",
        "             ####        ####",
        "           ######        ######",
        "##############################################################              ##################################",
        "#...#......#.##...#......#.##...#......#.##------------------#              #...#......#.##------------------#",
        "###########################################------------------#              ###############------------------#",
        "#..#....#....##..#....#....##..#....#....#####################              #..#....#....#####################",
        "##########################################    #----------#                  ##############    #----------#",
        "#.....#......##.....#......##.....#......#    #----------#                  #.....#......#    #----------#",
        "##########################################    #----------#                  ##############    #----------#",
        "#.#..#....#..##.#..#....#..##.#..#....#..#    #----------#                  #.#..#....#..#    #----------#",
        "##########################################    ############                  ##############    ############",
    ]

    # Print the pattern line by line
    for line in pattern:
        print(line)


# Call the function to print the pattern
print_pattern()


"""
调格式非常麻烦，又没什么技术含量，谁爱做谁做。
于是我找chatGPT老师要了标准程序。他爱不爱做我不知道，起码做得挺快的。
他甚至还做了个模块化，把东西都放进了函数print_pattern里面，我哭死，就拿他做模块化的例子吧。
你应该知道怎么把他改成不自定义函数的形式吧？
"""
