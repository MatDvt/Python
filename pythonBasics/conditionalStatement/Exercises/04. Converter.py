number = float(input())
input_metrics = input()
output_metrics = input()

result = 0

if input_metrics == 'm' and output_metrics == 'mm':
    result = number * 1000
    print(f'{result:.3f}')
elif input_metrics == 'm' and output_metrics == 'cm':
    result = number * 100
    print(f'{result:.3f}')
elif input_metrics == 'mm' and output_metrics == 'm':
    result = number / 1000
    print(f'{result:.3f}')
elif input_metrics == 'mm' and output_metrics == 'cm':
    result = number / 10
    print(f'{result:.3f}')
elif input_metrics == 'cm' and output_metrics == 'mm':
    result = number * 10
    print(f'{result:.3f}')
elif input_metrics == 'cm' and output_metrics == 'm':
    result = number * 100
    print(f'{result:.3f}')
