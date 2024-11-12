#include <filesystem>

struct programArgs {
    int lower;
    int upper;
    int numbers;
    int special;
};

struct dataset {
    char* data[93];
    int length;
};

void createDataset(programArgs* args, dataset* data){
    int currentIndex = 0;
    if (args->lower == 1){
        const char* charalist = "abcdefghijklmnopqrstuvwxyz";
        for(currentIndex; currentIndex < currentIndex + 26; currentIndex++){
            *data->data[currentIndex] = charalist[currentIndex];
        };
        data->length += 26;
    };
    if (args->lower == 1){
        const char* charalist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for(currentIndex; currentIndex < currentIndex + 26; currentIndex++){
            *data->data[currentIndex] = charalist[currentIndex];
        };
        data->length += 26;
    };
    if (args->lower == 1){
        const char* charalist = "0123456789";
        for(currentIndex; currentIndex < currentIndex + 10; currentIndex++){
            *data->data[currentIndex] = charalist[currentIndex];
        };
        data->length += 10;
    };
    if (args->lower == 1){
        const char* charalist = "!@#$%^&*()-_=+[]{}|;:\",.<>?/`~";
        for(currentIndex; currentIndex < currentIndex + 31; currentIndex++){
            *data->data[currentIndex] = charalist[currentIndex];
        };
        data->length += 31;
    };
}

char *_wgetcwd(char *path, int 256);

int _mkdir(const char *dirname){

}
