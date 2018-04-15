/*
  Coded By : Medi Assumani
  Language : Java
  Topic : Linked List

  Purpose : Implementing The Linked List Data Structure from scratch
*/
import java.util.*;
import java.io.IOException;
/*
  * The Node class acts as an helper class for the Linked List Class
  * @param AnyType : The generuc parameter type . e,g : Interger, String, Double
*/
class LinkedList<AnyType>{

  private static class Node<AnyType>{

      private AnyType data;
      private Node<AnyType> next;

      public Node(AnyType data){
          this.data = data;
          this.next = null;
        }

  } //  end of the Node Class

  private Node<AnyType> head;

  public LinkedList(){
      head = null;
    }

  /*
  This function checks wheater or not the list is empty by returning a true or false value
  Time Complexity :
  */
  public boolean isEmpty(){
      return this.head == null;
    }

  /* Function to insert a new elemnt in the tail of the list
    Time Complexity :
  */
   public void append(AnyType data){
     if (this.isEmpty()) {
       this.prepend(data);
       return;

     }
     Node<AnyType> currentNode = this.head;
     while (currentNode.next != null){
       currentNode = currentNode.next;
     }
     currentNode.next = new Node<AnyType>(data);

   }
  /* This function inserts new element at the head of the list
    Time Complexity :
  */
   public void prepend(AnyType data){

    Node <AnyType> new_node = new Node<AnyType> (data);
    new_node.next = this.head;
    head = new_node;
   }
   /*
   This funcion parses through each node and prints the element
   Time Complexity :

   */
   public void print(){

     if(this.isEmpty()){
       System.out.println("The list is Empty.");
       System.exit(0); // terminates/exits out the program
     }
     try{

       Node<AnyType> temp = this.head;
       while(true){
         System.out.println(temp.data);
          if(temp.next != null){
            temp = temp.next;
          }else{
            break;
          }
       }
     } catch (NullPointerException e){
       System.out.println("Error Found : Null value");
     }

   }
   /*
   This function parses through the entire list to counts the length
   Time Complexity :
   */
   public int length(){

     int counter = 0;
     if(this.isEmpty()){
       return 0;
     }
     try{

       Node <AnyType> temp = this.head;
       counter = 1;//because the head already counts as one elemnt
       while(temp.next != null){
         temp = temp.next;
         counter++;
       }
     } catch(NullPointerException e){
       System.out.println("Error : Null Pointer found");
     }
     return counter;
   }

   /*
   Function to delete an elemnt from the List at a given position
   Time Complexity :
   @param data : The item to be deletd from the list
   */

   public void delete(AnyType data){
     if(this.isEmpty()){
       System.out.println("The List is Empty.");
       System.exit(0);
     }

     try{
       Node<AnyType> temp = this.head;
       while()


     }catch (NullPointerException e){
       System.out.println("Error : Null Pointer found")
     }

   }

   /*
    Function to replace a data with a different one
    Time Complexity :
    @param  oldData : The data that has to be replaed
    @param newData : The data that has to replace the old data
   */

   public void replace(AnyType oldData, AnyType newData){
     if(this.isEmpty()){
       System.out.println("The List is Empty");
     }
     Node<AnyType> temp = this.head;
     while(temp.next != null){
       if(temp.data == oldData){
         temp.data = newData;
       }else{
         temp = temp.next;
       }
     }
   }

}
