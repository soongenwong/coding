class CustomStack {
public:
    int n;
    stack<int> stack;
    vector<int> inc;

    CustomStack(int n) {
        this->n = n;
    }

    void push(int x) {
        if (stack.size() < n) {
            stack.push(x);
            inc.push_back(0);
        }
    }

    int pop() {
        if (stack.empty()) return -1;
        if (inc.size() > 1) inc[inc.size() - 2] += inc.back();
        int res = stack.top() + inc.back();
        stack.pop();
        inc.pop_back();
        return res;
    }

    void increment(int k, int val) {
        if (!stack.empty()) {
            int idx = min(k, (int)inc.size()) - 1;
            inc[idx] += val;
        }
    }
};


// final solution 
// inc helps defer the incrementing until it's actually needed, saving time.

// pop ensures cumulative increments "bubble down" the stack so that no multiple traversals are necessary.

// All operations are performed in constant time.