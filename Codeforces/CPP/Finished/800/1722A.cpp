#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define endl "\n"
#define forn(i, n) for(int i = 0; i < int(n); i++)

void solve() {
    int length;
    cin >> length;
    string s;
    cin >> s;
    if(length != 5) {
        cout << "NO" << endl;
    }
    else {
        set<char> set;
        for(int i = 0; i < length; i++) {
            char currentChar = s.at(i);
            set.insert(currentChar);
        }
        if(set.contains('T') && set.contains('i') && set.contains('m') && set.contains('u') && set.contains('r')) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}

int main()
{
    int t;
    cin >> t;
    forn(i, t) {
        solve();
    }
    return 0;
}