public class LinkedListTester{
  public static void main(String[] args){

          // Testing the LinkedList methods

      LinkedList<String> classOneStudents = new LinkedList<String>();
      classOneStudents.append("Medi Assumani");
      classOneStudents.append("Ahmed Ahmed");
      classOneStudents.append("Michal Shepard");
      classOneStudents.append("Yves Songolo");
      classOneStudents.append("Maceline Ambroise");

      System.out.println("The Length is : " + classOneStudents.length());
      classOneStudents.print();
      classOneStudents.delete("Yves Songolo");
      System.out.println("The Length is : " + classOneStudents.length());
      classOneStudents.print();


  }
}
