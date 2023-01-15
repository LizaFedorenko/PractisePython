from factorial.factorial import fact
from exponentiation.exponentiation import exp2, exp3
from exponentiation.root import root2, root3
from logarithm.logarithm import log, lg, ln
def main():
    try:
     print('List of functions: factorial, exp2, exp3, root2, root3, log, lg, ln')
     ask = input('Input function: ')
     if ask == 'exp2':
         n = float(input('Number: '))
         print(exp2(n))
     elif ask == 'factorial':
         n = float(input('Number: '))
         print(fact(n))
     elif ask == 'exp3':
         n = float(input('Number: '))
         print(exp3(n))
     elif ask == 'root2':
         n = float(input('Number: '))
         if n < 0:
             print('Error')
         else:
             print(root2(n))
     elif ask == 'root3':
         n = float(input('Number: '))
         if n < 0:
             print('Error')
         else:
             print(root3(n))
     elif ask == 'log':
         a = float(input('a: '))
         if (a<=0) or a == 1:
             print('Error')
         b = float(input('b: '))
         if b <= 0:
             print('Error')
         print(log(a , b))
     elif ask == 'lg':
         b = int(input('b: '))
         if b <= 0:
             print('Error')
         print(lg(b))
     elif ask == 'ln':
         b = float(input('b: '))
         if b <= 0:
             print('Error')
         print(ln(b))
     else:
         print('Input error')
    except:
        print('Error!')
if __name__ == '__main__':
    main()