/*
数组（array）是一种线性数据结构
将元素在数组中的位置称为该元素的索引（index）

数组下标都是从0开始的。
数组内存空间的地址是连续的


//1.初始化数组

#include<iostream>
using namespace std;
int main()
{
	int arr[5];
	int nums[5] = { 1,3,2,5,4 };

	int* arr1 = new int[5];
	int* nums1 = new int[5] {1, 3, 2, 5, 4};


	return 0;
}

// 2.数组的随机访问
int randomAccess(int* nums, int size) {
	int randomIndex = rand() % size;
	int randomNum = nums[randomIndex];
	return randomNum;
}

// 3.数组的插入、删除、遍历、查找、扩容
void insert(int* nums, int size, int num, int index) {
	for (int i = size - 1; i > index; i--) {
		nums[i] = nums[i - 1];
	}
	nums[index] = num;
}

void remove(int* nums, int size, int index) {
	for (int i = index; i < size - 1; i++) {
		nums[i] = nums[i + 1];
	}
}

void traverse(int* nums, int size) {
	int count = 0;
	for (int i = 0; i < size; i++) {
		count += nums[i];
	}
}

int find(int* nums, int size, int target) {
	for (int i = 0; i < size; i++) {
		if (nums[i] == target) {
			return i;
		}
	}
	return -1;
}

int* extend(int* nums, int size, int enlarge) {
	int* res = new int[size + enlarge];
	for (int i = 0; i < size; i++) {
		res[i] = nums[i];
	}
	delete[]nums;
	return res;
}

//二分查找
//1.左闭右闭
class Solution {
public:
	int search(vector<int>& nums, int target) {
		int left = 0;
		int right = nums.size() - 1; // 定义target在左闭右闭的区间里，[left, right]
		while (left <= right) { // 当left==right，区间[left, right]依然有效，所以用 <=
			int middle = left + ((right - left) / 2);// 防止溢出 等同于(left + right)/2
			if (nums[middle] > target) {
				right = middle - 1; // target 在左区间，所以[left, middle - 1]
			}
			else if (nums[middle] < target) {
				left = middle + 1; // target 在右区间，所以[middle + 1, right]
			}
			else { // nums[middle] == target
				return middle; // 数组中找到目标值，直接返回下标
			}
		}
		// 未找到目标值
		return -1;
	}
};

//2.左闭右开
class Solution {
public:
	int search(vector<int>& nums, int target) {
		int left = 0;
		int right = nums.size(); // 定义target在左闭右开的区间里，即：[left, right)
		while (left < right) { // 因为left == right的时候，在[left, right)是无效的空间，所以使用 <
			int middle = left + ((right - left) >> 1);
			if (nums[middle] > target) {
				right = middle; // target 在左区间，在[left, middle)中
			}
			else if (nums[middle] < target) {
				left = middle + 1; // target 在右区间，在[middle + 1, right)中
			}
			else { // nums[middle] == target
				return middle; // 数组中找到目标值，直接返回下标
			}
		}
		// 未找到目标值
		return -1;
	}
};
*/

#include <iostream>
using namespace std;
long long feibo(int n) {
	int a1 = 0;
	int a2 = 1;
	for (int i = 1; i < n; i++) {
		a1 = a2;
		a2 = a1 + a2;
	}
	return a1;
}
int main() {
	int n;
	cin >> n >> endl;
	int sum = feibo(n);
	cout << sum << endl;
	return 0；
}


























