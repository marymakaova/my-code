#include <iostream>
#include <vector>
#include <cmath>
#include <utility>

using namespace std;
int main(){
    int n;
    cin >> n;
    //int len = (int) sqrt(n) + 1;
    //вектор с составными делителями
    vector<bool> sieve(n + 1, true);
    //заведомо считаем все числа (индексы) простыми
    //0 и 1 - не простые делители
    sieve[0] = false;
    sieve[1] = false;
    for(int i = 2; i * i <= n; i++){
        if(sieve[i]){
            //начинаем с i*i так как все кратные до уже были вычеркнуты
            for(int j = i * i; j <= n; j += i){
                //так как мы идем с шагом делителя, то мы придем на индекс кратного числа и вычеркнем его
                sieve[j] = false;
            }
        }
    }
    //вектор простыми делителями числа
    vector<int> prime_del(sieve.size());
    for(int i = 2; i < sieve.size(); i++){
        if(sieve[i]){
            prime_del.push_back(i);
        }
    }
    //копия n, чтобы не изменять само число (вдруг оно простое, и тогда в конце нужно просто его вывести)
    int temp_n = n;
    //какой-то крутой тип данных pair, все элементы в нем состоят из пар. в моем случае это простое число и его степень для вывода
    vector<pair<int, int>> finaly_del;
    for(int i = 0; i < n; i++){
        if (sieve[i]) { 
            int cnt = 0;
            //делим n на простое число пока делится, cnt - степень числа, i - простой делитель из sieve
            while(temp_n % i == 0){
                ++cnt;
                temp_n /= i;
            }
            if(cnt > 0){
                finaly_del.push_back({i, cnt});
            }
    }
    }
    //как раз проверка на наличие делителей
    if (finaly_del.empty()) {
        cout << n << endl;
        return 0;
    }
    //вывод
    for(int i = 0; i < finaly_del.size(); i++){
        cout << finaly_del[i].first;
        if(finaly_del[i].second > 1){
            cout << '^' << finaly_del[i].second;
        }
        if(i < finaly_del.size() - 1){
            cout << '*';
        }
    }
    return 0;
    
}