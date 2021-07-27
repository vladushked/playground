/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };

 [6,3,4,9,0,2,1,6,2,8,1,2,6,3,5,0,7,8,1]

 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head == NULL)
            return NULL;

        ListNode *current = head;
        ListNode *left = head;
        ListNode *right = head;

        int i = 1;
        int k = 1;
        int delta = 0;

        while (i <= n && current->next && current) {
            if (i % n == 0) {
                right = current;
                k = i;
            }
            current = current->next;
            i++;
        }

        while (current->next && current) {
            if (i % n == 0) {
                left = right;
                right = current;
                delta = 0;
                k = i;
            }
            current = current->next;
            i++;
            delta++;
        }

        while (delta > 0) {
            left = left->next;
            delta--;
        }

        if (n == i) {
            if (i == 1) {
                delete head;
                head = NULL;
            } else {
                left = left->next;
                head = left;
            }
        } else if (n > 1) {
            right = left->next->next;
            delete left->next;
            left->next = right;
        } else {
            delete left->next;
            left->next = NULL;
        }

        return head;
    }
};