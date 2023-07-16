import java.util.concurrent.atomic.AtomicInteger;

class Foo {

    AtomicInteger fisrtJobDone = new AtomicInteger(0);
    AtomicInteger secondJobDone = new AtomicInteger(0);

    public Foo() {}

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        fisrtJobDone.incrementAndGet();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (fisrtJobDone.get() != 1) {}
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        secondJobDone.incrementAndGet();
    }

    public void third(Runnable printThird) throws InterruptedException {
        while(secondJobDone.get() != 1) {}
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
