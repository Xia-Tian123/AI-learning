//定义
struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x):val(x),next(nullptr){}
};

//1.   初始化链表
int main() {
	ListNode* n0 = new ListNode(1);
	ListNode* n1 = new ListNode(3);
	ListNode* n2 = new ListNode(2);
	ListNode* n3 = new ListNode(5);
	ListNode* n4 = new ListNode(4);
	n0->next = n1;
	n1->next = n2;
	n2->next = n3;
	n3->next = n4;
}


//2.   插入节点 只需改变两个节点引用（指针）即可，时间复杂度为 𝑂(1)
void insert(ListNode* n0, ListNode* p) {
	ListNode* n1 = n0->next;
	p->next = n1;
	n0->next = p;
}

//3.   删除节点 只需改变一个节点的引用（指针）即可
void remove(ListNode* n0) {
	if (n0->next == nullptr)
		return;
	ListNode* p = n0->next;
	ListNode* n1 = p->next;
	n0->next = n1;
	delete p;
}

//4.   访问节点 时间复杂度为 𝑂(𝑛)
ListNode *access(ListNode *head,int index) {
	for (int i = 0; i < index; i++) {
		if (head == nullptr)
			return nullptr;
		head = head->next;
	}
	return head;
}

//5.   查找节点
int find(ListNode* head, int target) {
	int index = 0;
	while (head != nullptr) {
		if (head->val == target)
			return index;
		head = head->next;
		index++;
	}
	return -1;
}