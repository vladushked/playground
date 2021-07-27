/**
* Definition for singly-linked list.
* struct ListNode {
* int val;
* ListNode *next;
* ListNode() : val(0), next(nullptr) {}
* ListNode(int x) : val(x), next(nullptr) {}
* ListNode(int x, ListNode *next) : val(x), next(next) {}
* };
*/
class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        return reverseListRec(head);
    }

    ListNode *reverseListRec(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }

        ListNode *rest = reverseListRec(head->next);

        head->next->next = head;
        head->next = NULL;

        return rest;
    }

    ListNode *reverseListIter(ListNode *head) {
        if (head == NULL)
            return NULL;
        if (head->next == NULL)
            return head;

        ListNode *it = head->next;
        ListNode *new_end = head;

        while (it && it->next) {
            ListNode *new_it = it->next;
            new_end->next = new_it;
            it->next = head;
            head = it;
            it = new_it;
        }

        it->next = head;
        head = it;
        new_end->next = NULL;
        return head;
    }
};