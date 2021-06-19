#include<iostream>

int main() {
    int n;
    std::cin >> n;
    int temp = n;
    int sum = 0;
    int ans = n;
    while(ans >= 10){
        while(temp > 0){
            int r = temp % 10;
            sum += r;
            temp = temp / 10;
        }
        ans = sum;
        temp = sum;
        sum = 0;
    }
    printf("%d", ans);
    return 0;
}