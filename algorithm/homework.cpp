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

#include <iostream>

/*
1.顺序队列的3个操作
#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	int *queue = new int[n];
	int front = 0, rear = 0, count = 0;   // count 记录当前队列元素个数

	// 尝试将 n+1 个整数顺序压入容量为 n 的队列
	for (int i = 0; i < n + 1; i++) {
		int x;
		cin >> x;
		if (count == n) {
			// 队列已满，入队操作不执行
			cout << "错误：队列已满。" << endl;
		} else {
			queue[rear] = x;
			rear = (rear + 1) % n;
			count++;
		}
	}

	// 执行 n+1 次取队首并出队操作
	for (int i = 0; i < n + 1; i++) {
		if (count == 0) {
			// 队列为空：取队首和出队都不执行
			cout << "错误：队列为空。" << endl;
			cout << -1 << endl;               // 空队列取队首返回 -1
			cout << "错误：队列为空。" << endl;
		} else {
			// 非空：取队首并出队，输出元素值
			cout << queue[front] << endl;
			front = (front + 1) % n;
			count--;
		}
	}

	delete[] queue;
	return 0;
}
	








2.出栈序列
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
	string in_seq, out_seq;
	cin >> in_seq >> out_seq;

	stack<char> st;
	string op;   //保存操作序列 P/O
	int i = 0;   //入栈指针
	int j = 0;   //出栈指针

	int n = in_seq.size();
	while (i < n)
	{
		//入栈
		st.push(in_seq[i]);
		op += 'P';
		i++;

		//只要栈顶等于目标出栈元素，持续出栈
		while (!st.empty() && st.top() == out_seq[j])
		{
			st.pop();
			op += 'O';
			j++;
		}
	}

	if (j == out_seq.size())
	{
		cout << "right\n";
		cout << op << "\n";
	}
	else
	{
		cout << "wrong\n";
		// stack只能取栈顶；要栈底到栈顶，需要辅助vector
		string remain;
		while (!st.empty())
		{
			remain = st.top() + remain;
			st.pop();
		}
		cout << remain << "\n";
	}
	return 0;
}
	


3.中缀表达式转后缀表达式
#include <iostream>
#include <stack>
#include <string>
#include <cctype>
using namespace std;

// 返回运算符优先级
int priority(char op) {
	if (op == '*' || op == '/') return 2;
	if (op == '+' || op == '-') return 1;
	return 0;  // '(' 的优先级最低，但不会参与比较
}

int main() {
	string s;
	cin >> s;

	stack<char> op;      // 运算符栈
	string output;       // 后缀表达式结果
	int i = 0;

	while (i < s.size()) {
		char c = s[i];

		if (isdigit(c)) {
			// 提取完整的多位数字
			string num;
			while (i < s.size() && isdigit(s[i])) {
				num += s[i];
				i++;
			}
			output += num + " ";
		} else if (c == '(') {
			op.push(c);
			i++;
		} else if (c == ')') {
			// 弹出运算符直到遇到左括号
			while (!op.empty() && op.top() != '(') {
				output += op.top();
				output += " ";
				op.pop();
			}
			if (!op.empty()) op.pop();  // 弹出左括号，不输出
			i++;
		} else {
			// 当前字符是运算符 + - * /
			while (!op.empty() && op.top() != '(' && priority(op.top()) >= priority(c)) {
				output += op.top();
				output += " ";
				op.pop();
			}
			op.push(c);
			i++;
		}
	}

	// 弹出栈中剩余的所有运算符
	while (!op.empty()) {
		output += op.top();
		output += " ";
		op.pop();
	}

	cout << output << endl;
	return 0;
}*/

































































