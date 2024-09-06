number_group = int(input())
number_case, number_improved = input().split()
percent_control_group = int(number_improved) / int(number_case) * 100
for i in range(number_group - 1):
    number_case, number_improved = input().split()
    percent_experimental_group = int(number_improved) / int(number_case) * 100
    if percent_experimental_group - percent_control_group > 5:
        print("better")
    elif percent_experimental_group - percent_control_group < -5:
        print("worse")
    else:
        print("same")
