public interface StackInterface<T>{
  public void push(); // inserts data of type T on top of the stack
  public T pop(); // removes the data of type T from top of the stack
  public T peepk(); // returns the data from top of the stack without deleting it
  public int length(); // returns an integer that determines the amount of elements in the stack
  public boolean isEmpty(); // returns True or False if the stack is empty
}
