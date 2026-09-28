#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>

//列表list
int main() {
	//1.   初始化列表
	//无初始值
	vector<int>num1;

	// 有初始值
	vector<int>nums = { 1,3,2,5,4 };



	//2.   访问元素
	int num = nums[1];
	nums[1] = 0;

	//3.   插入与删除元素
	//清空列表 
	nums.clear();
	//在尾部添加元素 
	nums.push_back(1);
	nums.push_back(3);
	nums.push_back(2);
	nums.push_back(5);
	nums.push_back(4);

	// 在中间插入元素 
	nums.insert(nums.begin() + 3, 6);

	// 删除元素 
	nums.erase(nums.begin() + 3);

	//4.   遍历列表
	// 通过索引遍历列表 
	int count = 0;
	for (int i = 0; i < nums.size(); i++) {
		count += nums[i];
	}

	//直接遍历列表元素 
	count = 0;
	for (int num : nums) {
		count += num;
	}


	//5.   拼接列表
	vector<int> nums1 = { 6,8,7,10,9 };
	nums.insert(nums.end(), nums1.begin(), nums1.end());


	//6.   排序列表
	sort(nums.begin(), nums.end());





	return 0;
}

/*66. 加一
给定一个表示 大整数 的整数数组 digits，
其中 digits[i] 是整数的第 i 位数字。
这些数字按从左到右，从最高位到最低位排列。
这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	vector<int>plusOne(vector<int>& digits) {
		int carry = 1;
		for (int i = digits.size() - 1; i >= 0 && carry; i--) {
			int sum = digits[i] + carry;
			digits[i] = sum % 10;
			carry = sum / 10;
		}
		if (carry) {
			digits.insert(digits.begin(), 1);
		}
		return digits;
	}
};*/


/* 链表节点结构体 */
struct ListNode {
	int val;         // 节点值
	ListNode* next;  // 指向下一节点的指针
	ListNode(int x) : val(x), next(nullptr) {}  // 构造函数
};



//206. 反转链表
//方法一：迭代（双指针）
class Solution {
public:
	ListNode *reverseList(ListNode* head) {
		ListNode *cur = head, *pre = nullptr;
		while (cur != nullptr) {
			ListNode* tmp = cur->next;
			cur->next = pre;
			pre = cur;
			cur = tmp;
		}
		return pre;
	}
};


//方法二：递归
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		return recur(head, nullptr);
	}
private:
	ListNode* recur(ListNode* cur, ListNode* pre) {
		if (cur == nullptr) return pre;
		ListNode* res = recur(cur->next, cur);
		cur->next = pre;
		return res;
	}
};