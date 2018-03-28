public class LinkedListTester{
  public static void main(String[] args){

          // Testing the LinkedList methods

      LinkedList<String> classOneStudents = new LinkedList<String>();
      classOneStudents.append("Medi Assumani");
      classOneStudents.append("Ahmed Ahmed");
      classOneStudents.append("Michal Shepard");
      classOneStudents.append("Yves Songolo");
      classOneStudents.append("Maceline Ambroise");

      System.out.println("Is the List Empty : " + classOneStudents.isEmpty());
      System.out.println("The Length is : " + classOneStudents.length());
      classOneStudents.print();
      classOneStudents.delete("Yves Songolo");
      classOneStudents.replace("Patrick Fortune","Medi Assumani");
      System.out.println("The Length is now : " + classOneStudents.length());
      classOneStudents.print();


  }
}
