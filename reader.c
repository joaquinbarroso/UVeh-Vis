#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* search_file(const char *filename, const char *search_string, int *result_size) {
    FILE *file = fopen(filename, "r");
    if (file != NULL) {
        int buffer_size = 256;
        int result_capacity = 10;
        int *result = (int*)malloc(result_capacity * sizeof(int));
        *result_size = 0;

        char buffer[buffer_size];
        int line_number = 1;

        while (fgets(buffer, buffer_size, file) != NULL) {
            if (strstr(buffer, search_string) != NULL) {
                if (*result_size >= result_capacity) {
                    result_capacity *= 2;
                    result = (int*)realloc(result, result_capacity * sizeof(int));
                }
                result[(*result_size)++] = line_number;
            }
            line_number++;
        }

        // Add the total number of lines to the indexes list
        if (*result_size >= result_capacity) {
            result_capacity *= 2;
            result = (int*)realloc(result, result_capacity * sizeof(int));
        }
        result[(*result_size)++] = line_number - 1; // Subtract 1 to get the correct total number of lines

        fclose(file);
        return result;
    } else {
        printf("Failed to open file: %s\n", filename);
        *result_size = -1;
        return NULL;
    }
}

char** export_lines(const char* filename, int* num_lines) {
    FILE* file = fopen(filename, "r");
    if (file != NULL) {
        char** lines = NULL;
        size_t buffer_size = 256;
        size_t num_lines_allocated = 10; // Initial capacity for the lines array
        *num_lines = 0;

        lines = (char**)malloc(num_lines_allocated * sizeof(char*));

        char buffer[buffer_size];
        while (fgets(buffer, buffer_size, file) != NULL) {
            // Allocate memory for the current line
            lines[*num_lines] = (char*)malloc((strlen(buffer) + 1) * sizeof(char));
            strcpy(lines[*num_lines], buffer);
            (*num_lines)++;

            // Resize lines array if needed
            if (*num_lines >= num_lines_allocated) {
                num_lines_allocated *= 2;
                lines = (char**)realloc(lines, num_lines_allocated * sizeof(char*));
            }
        }
        fclose(file);
        return lines;
    } else {
        printf("Failed to open file: %s\n", filename);
        *num_lines = -1;
        return NULL;
    }
}



