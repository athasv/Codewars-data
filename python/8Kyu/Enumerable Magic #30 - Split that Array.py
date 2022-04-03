def partition(arr, classifier_method):
        return [i for i in arr if classifier_method(i) == True], [i for i in arr if classifier_method(i) == False]