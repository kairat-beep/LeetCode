#include <vector>
using namespace std;
class NumMatrix
{
public:
  vector<vector<int>> rangeSums;
//Block sum like Dyn Prog O(N), all elements individually.
  NumMatrix(vector<vector<int>>& matrix)
  {
    vector<int> firstRow {matrix[0][0]};
    for(int i =1; i < matrix[0].size(); i++)
    {
      firstRow.push_back(firstRow.back() + matrix[0][i]);
    }
    rangeSums.push_back(firstRow);
    for (int i = 1; i < matrix.size(); i++)
    {
      int leftSum=0;
      vector<int> temporal;
      for(int j = 0; j < matrix[0].size(); j++)
      {
        leftSum += matrix[i][j];
        temporal.push_back(rangeSums[i-1][j] + leftSum);
      }
      rangeSums.push_back(temporal);
    }
  }

  int sumRegion(int row1, int col1, int row2, int col2)
  {
    int left=0,top=0,leftTop=0,
        interX = -1, interY=-1;
    //Get summ of the full block(bot-left), Subtract Left, Subtract Top, Add Intersection
    //Get TOP section
    if(row1>0)
    {
      top = rangeSums[row1-1][col2];
      interY = row1-1;
    }
    //get LEFT section
    if(col1>0)
    {
      left = rangeSums[row2][col1-1];
      interX=col1-1;
    }
    //get INTERSECTION
    if(interX !=-1 and interY!= -1)
    {
      leftTop = rangeSums[interY][interX];
    }
    return rangeSums[row2][col2] +leftTop - left - top;
  }
};

#include <gtest/gtest.h>

vector<vector<int>> toTest
{
  {1,2,3,4,5,6},
  {7,8,9,10,11,12},
  {13,14,15,16,17,18},
  {19,20,1,2,3,4}
};

// Demonstrate some basic assertions.
TEST(RangeSum, EdgeIncluded)
{
  NumMatrix solution(toTest);
  EXPECT_EQ(solution.sumRegion(1,0,2,1),42);
}
TEST(RangeSum, 2Square)
{
  NumMatrix solution(toTest);
  EXPECT_EQ(solution.sumRegion(1,3,2,4),54);
}
TEST(RangeSum, OneSquare)
{
  NumMatrix solution(toTest);
  EXPECT_EQ(solution.sumRegion(1,1,1,1),8);
  EXPECT_EQ(solution.sumRegion(1,0,1,0),7);
  EXPECT_EQ(solution.sumRegion(2,5,2,5),18);
  EXPECT_EQ(solution.sumRegion(3,1,3,1),20);
}
TEST(RangeSum, Corner)
{
  NumMatrix solution(toTest);
  EXPECT_EQ(solution.sumRegion(0,0,0,0),1);
  EXPECT_EQ(solution.sumRegion(0,5,0,5),6);
  EXPECT_EQ(solution.sumRegion(3,0,3,0),19);
  EXPECT_EQ(solution.sumRegion(3,5,3,5),4);
}

