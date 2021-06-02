using System.Threading;

public class FooBar {
    private int n;
    private static readonly Semaphore semaphore1 = new Semaphore(1,1);
    private static readonly Semaphore semaphore2 = new Semaphore(0,1);
    
    public FooBar(int n) {
        this.n = n;
    }

    public void Foo(Action printFoo) {
        
        for (int i = 0; i < n; i++) {
            semaphore1.WaitOne();
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            semaphore2.Release();
        }
    }

    public void Bar(Action printBar) {
        
        for (int i = 0; i < n; i++) {
            semaphore2.WaitOne();
            // printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            semaphore1.Release();
        }
    }
}
