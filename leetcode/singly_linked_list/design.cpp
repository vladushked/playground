struct SinglyListNode {
    int val;
    SinglyListNode *next;

    SinglyListNode(int x) : val(x), next(nullptr) {}

    SinglyListNode(int x, SinglyListNode *next_node) : val(x), next(next_node) {}
};

class MyLinkedList {
public:
/** Initialize your data structure here. */
    MyLinkedList() {
        head = nullptr;
        tail = nullptr;
        size = 0;
    }

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index >= size || index < 0) {
            return -1;
        } else {
            SinglyListNode *it = head;

            for (int i = 0; i < index; i++) {
                it = it->next;
            }
            return it->val;
        }
    }

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        SinglyListNode *new_node;
        if (size == 0) {
            new_node = new SinglyListNode(val);
            tail = new_node;
        } else {
            new_node = new SinglyListNode(val, head);
        }
        head = new_node;
        size++;
    }

/** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        SinglyListNode *new_node = new SinglyListNode(val);
        if (size == 0) {
            head = new_node;
        } else {
            tail->next = new_node;
        }
        tail = new_node;
        size++;
    }

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        } else if (index == size) {
            this->addAtTail(val);
        } else {
            SinglyListNode *it = head;

            for (int i = 0; i < index - 1; i++) {
                it = it->next;
            }

            SinglyListNode *new_node;
            if (size == 1) {
                new_node = new SinglyListNode(val, it);
                head = new_node;
            } else {
                new_node = new SinglyListNode(val, it->next);
                it->next = new_node;
            }
            size++;
        }
    }

/** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index < size) {
            if (size > 1) {
                SinglyListNode *it = head;

                if (index == 0) {
                    SinglyListNode *to_del = head;
                    head = head->next;
                    delete to_del;
                } else {
                    for (int i = 0; i < index - 1; i++) {
                        it = it->next;
                    }

                    SinglyListNode *left = it;
                    it = it->next;

                    if (index == size - 1) {
                        tail = left;
                        tail->next = nullptr;
                    } else {
                        SinglyListNode *right = it->next;
                        left->next = right;
                    }


                    delete it;
                }

            } else {
                delete head;
                head = nullptr;
                tail = nullptr;
            }
            size--;
        }
    }

    SinglyListNode *head;
    SinglyListNode *tail;
    int size;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */