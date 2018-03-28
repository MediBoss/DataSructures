/*
  Coded By : Medi Assumani
  Language : Java
  Topic : List (resizable) that only supports the Int Data Type

  Purpose : Re-building Java's Arraylist with more functionalities and practicing algorithm skills
*/
import java.util.Arrays;
import java.lang.Class;

// implementing the List Data Structure where E is the Data Type
public class JavaList<E>{

  private int size = 0;
  private static final int DEFAULT_CAPACITY = 10;
  private Object elements[]; // an array of the Object Class

  //constructor for List Objec with initial size
  //@ param size : the length of the List
  public JavaList(int size){
      // this initializes the created List with a starting length of DEFAULT_CAPACITY
    elements = new Object[DEFAULT_CAPACITY]
  }

  //Function to return the size of the List
  public int getLength(){
    return this.size;
  }

  // Function expend the size of the List by a factor of Two
  public void maximizeListCapacity(){
    int newListSize = this.elements.length * 2;
    this.elements = Arrays.copyOf(elements,newListSize); // creates a copy of a new array with new size
  }
  // Function to append an element in the List
  public void addElement(E e){
    if(size == elements.length){

    }
  }
  // function to remove an element in the list
  public void deleteElement(int elemnt){

  }
  /*
    function to set an elemnt in the list on a given position
    @param : element :
    @param : position:
  */
  public void setElementInPosition(int element, int position){

  }
  public int getElementInPosition(){

     return 0;
  }
    /*
      Function to search if an elemnt is in the list
      @param elemToBeSearched :
    */
  public bool search(int elemToBeSearched){

    return true;
  }
  // function to sort the List
  public void sort(){

  }

}
