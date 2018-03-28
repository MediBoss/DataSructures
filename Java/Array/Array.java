/*
  Coded By : Medi Assumani
  Language : Java
  Topic : 1 and 2 Dimentional Arrays in Java

*/
public class Array{
  public static void main(String[] args){

          // ONE DIMENSIONAL ARRAY

      //declaring + initilizing an array
    int [] testScores = {90,89,98,45,76,90,34};
      // geting the size of the array
    int testNumbers = testScores.length;
      //getting a value of an array at at specific index
    int firstScore = testScores[0];
      //Changing Array value at a specific index
    testScores[3] = 78;

            // 2D ARRAY

      int [][] matrix = new int [2][2]; // 2d array with 2 rows and 2 columns
      matrix = {{2,5},{5,8}}; // initializing a 2d array

        //Printing each element of the matrix
      for(int j = 0; j < 2; j++){
        for(int k = 0; k < 2; k++){
          System.out.println(matrix[j][k])
        }
      }
  }
}
