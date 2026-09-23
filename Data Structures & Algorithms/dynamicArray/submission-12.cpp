class DynamicArray {
public:
    int *arr;
    int cap;
    int pTail = -1;
    DynamicArray(int capacity) {
        cap = capacity;
        arr = new int[cap];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if(pTail >= cap - 1){
            resize();
        }
        pTail++;
        arr[pTail] = n;
    }

    int popback() {
        cout << pTail << endl;
        return arr[pTail--];
    }

    void resize() {
        int *tempArray = new int[2*cap];
        for(int i = 0; i < cap; i++){
            tempArray[i] = arr[i];
            pTail = i;
        }
        cap = cap * 2;
        cout << cap << endl;
        delete [] arr;
        arr = tempArray;
        
    }

    int getSize() {
        return pTail + 1;
    }

    int getCapacity() {
        return cap;
    }
};
