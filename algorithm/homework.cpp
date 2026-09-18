//7-1 第n项斐波那契数的计算


/*
//法一：循环
#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;//cin不能和endl一起

	if (n == 0 || n == 1) {   //注意判断等于两个等号
		cout << 1 << endl;
		return 0;
	}

	long long a = 1, b = 1, c;//注意数据类型

	for (int i = 2; i <= n; ++i) {
		c = a + b;
		a = b;
		b = c;
	}

	cout << b << endl;

	return 0;
}


//法二：递归+记忆化（要注意为什么时间复杂度变小了）
#include <iostream>
using namespace std;

long long nums[92] = { 0 };

long long fib(int n) {
	if (n == 0 || n == 1) return 1;
	if (nums[n] != 0) return nums[n];
	return nums[n] = fib(n - 1) + fib(n - 2);
}
int main() {
	int n;
	cin >> n;
	cout << fib(n) << endl;

	return 0;
}

*/

//7-2 最大公约数和最小公倍数

/*
	//for (int i = n; 1<= i <= n; --i) 这个不能这么写，1<=i会被看成是一个比较表达式，返回1或0


//欧几里得算法求最大公约数

#include <iostream>
using namespace std;

int gcd(int a, int b) {
	while (b != 0) {
		int t = a % b;
		a = b;
		b = t;
	}
	return a;
}

int main() {
	int m, n;
	cin >> m >> n;

	int g = gcd(m, n);
	int l = m / g * n;// 最小公倍数（先除后乘，防止溢出）

	cout << g << " " << l << endl;
	return 0;
}

*/

/*7-1 冰雹猜想
冰雹猜想的内容是：任何一个大于1的整数n，按照n为偶数则除等2，n为奇数则乘3后再加1的规则不断变化，最终都可以变化为1。

例如，n等于20，变化过程为：20、10、5、16、8、4、2、1。编写程序，用户输入n，输出变化过程以及变化的次数。

#include <iostream>
using namespace std;

int main() {
    long long n;
    cin >> n;

    int count = 1;
    cout << n;

    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
        cout << " " << n;
        count++;
    }

    cout << "\ncount = " << count << endl;
    return 0;
}*/


/*7-2 顺序表区间数据求和
#include <iostream>
#include <vector>
using namespace std;
int main() {
	int n,x,y;
	cin >> n;
	vector <int> sums(n);
	for (int i = 0; i < n; i++) {
		cin>>sums[i];
	}
	cin >> x >> y;
	int count = 0;
	for (int i = 0; i < n; i++) {
		if (sums[i] <= y && sums[i] >= x) {
			count += sums[i];
		}
	}
	cout << count;
	return 0;
}*/

/*
7-3 一元多项式求导
#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	bool flag = false;  // 记录是否有输出过非零项

	for (int i = 0; i < n; i++) {
		int c, e;
		cin >> c >> e;

		if (e != 0) {                     // 常数项求导为0，跳过
			cout << c * e << " " << e - 1 << " ";
			flag = true;
		}
	}

	if (!flag) {                          // 一项都没输出，说明是零多项式
		cout << "0 0 ";
	}

	return 0;
}*/








