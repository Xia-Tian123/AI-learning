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