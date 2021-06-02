public class Foo {
    private bool first;
    private bool second;
    
    public Foo() {
        first = false;    
        second = false;
    }

    public void First(Action printFirst) {
        
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        Object lk = new Object();
        lock(lk)    {
            first = true;
        }
    }

    public void Second(Action printSecond) {
        
        // printSecond() outputs "second". Do not change or remove this line.
        while (!first) {}
        printSecond();
        
        Object lk = new Object();
        lock(lk)    {
            second = true;
        }
    }

    public void Third(Action printThird) {
        
        // printThird() outputs "third". Do not change or remove this line.
        while (!second) {}
        printThird();
    }
}
