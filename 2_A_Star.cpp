#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct node
{
    int hr;
    vector<vector<int>> sq;
    int r, c;
    
};

bool comp(node *p1, node *p2)
{
    if (p1->hr < p2->hr)
    {
        return true;
    }

    return false;
}
int level=0;
void Eight(vector<node *> &ol, vector<vector<int>> goal, int r, int c)
{
    cout<<"level:-"<<level ;
	cout<< "Heuristic Value : " << ol.front()->hr << endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << ol.front()->sq[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    if (ol.front()->sq == goal)
    {
        exit(0);
    }

    if (c + 1 < 3)
    {
        int count = 0;
        vector<vector<int>> test;
        test = ol.front()->sq;
        swap(test[r][c + 1], test[r][c]);

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (test[i][j] != goal[i][j])
                {
                    count++;
                }
            }
        }

        node *newnode = new node();
        newnode->sq = test;
        newnode->hr = count;
        newnode->r = r;
        newnode->c = c + 1;
        ol.push_back(newnode);
        count = 0;
    }

    if (c - 1 > -1)
    {
        int count = 0;
        vector<vector<int>> test;
        test = ol.front()->sq;
        swap(test[r][c - 1], test[r][c]);

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (test[i][j] != goal[i][j])
                {
                    count++;
                }
            }
        }

        node *newnode = new node();
        newnode->sq = test;
        newnode->hr = count;
        newnode->r = r;
        newnode->c = c - 1;
        ol.push_back(newnode);
        count = 0;
    }

    if (r + 1 < 3)
    {
        int count = 0;
        vector<vector<int>> test;
        test = ol.front()->sq;
        swap(test[r + 1][c], test[r][c]);

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (test[i][j] != goal[i][j])
                {
                    count++;
                }
            }
        }

        node *newnode = new node();
        newnode->sq = test;
        newnode->hr = count;
        newnode->r = r + 1;
        newnode->c = c;
        ol.push_back(newnode);
        count = 0;
    }

    if (r - 1 > -1)
    {
        int count = 0;
        vector<vector<int>> test;
        test = ol.front()->sq;
        swap(test[r - 1][c], test[r][c]);

        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (test[i][j] != goal[i][j])
                {
                    count++;
                }
            }
        }

        node *newnode = new node();
        newnode->sq = test;
        newnode->hr = count;
        newnode->r = r - 1;
        newnode->c = c;
        ol.push_back(newnode);
        count = 0;
    }

    ol.erase(ol.begin());

    while (!ol.empty() && level<40)
    {
        level++;
        sort(ol.begin(), ol.end(), comp);
        Eight(ol, goal, ol.front()->r, ol.front()->c);
    }
}

int main()
{
    int count = 0;
    vector<node *> ol;
    vector<int>val;
    vector<vector<int>> start;   //2d array
    /* {
        {1, 2, 3},
        {5, 6, 0},
        {7, 8, 4}};
    */
    vector<vector<int>> goal;
    /* {
        {1, 2, 3},
        {5, 6, 4},
        {7, 8, 0}};
    */
    int r , c,v;

    for(int i=0;i<3;i++)
    {
            cout<<"\nEnter start elements:-";
            for(int j=0;j<3;j++)
            {
                cin>>v;
                val.push_back(v);
            }
            start.push_back(val);
            val.clear();
    }
    for(int i=0;i<3;i++)
    {
            cout<<"\nEnter goal elements:-";
            for(int j=0;j<3;j++)
            {
                cin>>v;
                val.push_back(v);
            }
            goal.push_back(val);
            val.clear();
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (start[i][j]==0)
            {
                r=i;
                c=j;
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (start[i][j] != goal[i][j])
            {
                count++;
            }
        }
    }

    node *newnode = new node();
    newnode->sq = start;
    newnode->hr = count;
    ol.push_back(newnode);
    Eight(ol, goal, r, c);
    return 0;
}
