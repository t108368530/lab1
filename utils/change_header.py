from functools import reduce
from os import listdir, path, walk
from random import randint, random, uniform
from typing import Dict, List

import librosa
import numpy as np


class data_path:
    first_path: List[str] = []
    file_path: Dict[str, List[str]] = {}

    def __init__(self, low_bound: int, upper_bound: int, interval: int):
        pass

    def __get_first_path(self, low_bound, upper_bound, interval) -> List[str]:
        pass

    def __get_file_path(self,
                        paths: str = './',
                        limit: int = 1,
                        depth: int = 0) -> List[List[str]]:
        pass

    def __gen_file_path(self):
        def map_data(ggwp: str):
            pass

class gen_dataset_file_path(data_path):
    def __init__(self, low_bound, upper_bound, interval):
        self.first_path = self.__get_first_path(low_bound, upper_bound,
                                                interval)
        self.__first_path_name = [n.replace('./','') for n in self.first_path]
        self.train_test = self.__spilt_train_test()
        self.__gen_file_path()
    
    def __spilt_train_test(self):
        temp=[]
        temp2=[]
        for n in self.__first_path_name:
            if 'train'in n :
                temp.append(n)
            elif 'Test' in n :
                temp2.append(n)
        return temp ,temp2
    

    def __get_first_path(self, low_bound, upper_bound, interval):
        return reduce(
            lambda a, b: a + b,
            [[f"./train{i}", f"./pitchShiftTest{i}"]
             for i in range(low_bound, upper_bound + interval, interval)])

    def __get_file_path(self, paths='./', limit=1, depth=0):
        for root, dirs, files in walk(paths):
            if dirs or files:
                depth += 1
            if dirs and (depth <= limit):
                return (self.__get_file_path(path.join(root, d), limit, depth)
                        for d in dirs)
            if files:
                return [path.join(root, f) for f in files]

    def __gen_file_path(self):
        def map_data(ggwp):
            self.file_path[ggwp] = reduce(lambda a, b: a + b,
                                          self.__get_file_path(ggwp))

        list(map(map_data, self.first_path))


class features(gen_dataset_file_path):
    def __init__(self, sample_rate, low_bound, upper_bound, interval):
        super().__init__(low_bound, upper_bound, interval)
        self.sample_rate = sample_rate

    def __extract_features(self, path: str) -> np.ndarray:
        pass

    def creat(self, shape: int, file_path: Dict[str, List[str]]):
        pass


class creat_data_sets(features):
    def __init__(self,
                 sample_rate=3000,
                 low_bound=9000,
                 upper_bound=13000,
                 interval=1000,
                 method="Default"):
        super().__init__(
            sample_rate,
            low_bound,
            upper_bound,
            interval,
        )
        self.__get_one_file_path = self.file_path[self.first_path[0]][0]
        self.shape = self.__extract_features(self.__get_one_file_path).shape[0]
        self.__method = method
        self.final_data_sets = {}
        self.__switch = {'Default': self.__case1}
        self.creat(self.shape, self.file_path, self.__method)

    def __case1(self, shape, dataList):
        xArray = np.zeros([len(dataList), shape])
        yArray = np.zeros([len(dataList)])

        for index, file in enumerate(dataList):
            try:
                xArray[index] = self.__extract_features(file)
                yArray[index] = file.rsplit("/", 2)[1]
            except ValueError:
                print(index, file, ValueError)
        return (xArray, yArray)

    def __extract_features(self, path):
        try:
            #             print(self.sample_rate)
            X, sampleRate = librosa.load(
                path,
                sr=self.sample_rate,
                offset=0.0,
                res_type="kaiser_best",
                dtype=np.float32,
            )
            spectral_contrast_fmin = 0.5 * sampleRate * 2**(-6)
            #             print(sampleRate)
            mel = np.mean(librosa.feature.melspectrogram(X, sr=sampleRate).T,
                          axis=0)
            tonnetz = np.mean(
                librosa.feature.tonnetz(y=librosa.effects.harmonic(X),
                                        sr=sampleRate).T,
                axis=0,
            )
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sampleRate,
                                                 n_mfcc=40).T,
                            axis=0)
            mfcc_delta = librosa.feature.delta(mfccs)  # TONY
            mfcc_delta2 = librosa.feature.delta(mfccs, order=2)  # TONY
            stft = np.abs(librosa.stft(X))
            chroma = np.mean(librosa.feature.chroma_stft(S=stft,
                                                         sr=sampleRate).T,
                             axis=0)
            contrast = np.mean(librosa.feature.spectral_contrast(
                S=stft, sr=sampleRate, fmin=spectral_contrast_fmin).T,
                               axis=0)

            ###### ADD NEW FEATURES (SPECTRAL RELATED)##### 24-SEP
            cent = np.mean(librosa.feature.spectral_centroid(y=X,
                                                             sr=sampleRate).T,
                           axis=0)
            flatness = np.mean(librosa.feature.spectral_flatness(y=X).T,
                               axis=0)
            rolloff = np.mean(librosa.feature.spectral_rolloff(
                S=stft, sr=sampleRate).T,
                              axis=0)
            rms = np.mean(librosa.feature.rms(S=stft).T, axis=0)
            ext_features = np.hstack([
                mfccs,
                mfcc_delta,
                mfcc_delta2,
                chroma,
                mel,
                contrast,
                tonnetz,
                cent,
                flatness,
                rolloff,
                rms,
            ])
        except Exception as e:
            print("Error encountered while parsing file:%s ,Error : %s" %
                  (path, e))
            return None

        return np.array(ext_features)

    def creat(self, shape, file_path, method):
        kv = file_path
        for key in kv:
            self.final_data_sets[key] = self.__switch[method](shape, kv[key])


def save_to_npy(datas: Dict, method):
    def zScore(x):
        return (x - np.mean(x, axis=0)) / np.std(x, axis=0)

    for key in datas.keys():
        if 'train' in key:
            path = './pre-train'
        elif 'Test' in key:
            path = './pre-test'
        file_name = key.replace('./', '')
        x, y = datas[key][0], datas[key][1]
        random_indices = np.random.permutation(x.shape[0])
        x, y = x[random_indices], y[random_indices]
        data_npy_path = f"{path}/{method}/Data-{file_name}.npy"
        label_npy_path = f"{path}/{method}/Label-{file_name}.npy"
        np.save(data_npy_path, zScore(x))
        np.save(label_npy_path, y.astype(np.int))


def concatenate_npy(npy_path):
    train_all_data = np.load(f"./pre-train/Data-All.npy", allow_pickle=True)
    train_all_label = np.load(f"./pre-train/Label-All.npy", allow_pickle=True)
    test_all_data = np.load(f"./pre-test/Data-All.npy", allow_pickle=True)
    test_all_label = np.load(f"./pre-test/Label-All.npy", allow_pickle=True)
    for index, name in enumerate(npy_path):
        name = name.replace('./', '')
        if index % 2 == 0:
            temp1 = np.load(f"./pre-train/change_header/Data-{name}.npy",
                            allow_pickle=True)
            temp2 = np.load(f"./pre-train/change_header/Label-{name}.npy",
                            allow_pickle=True)
            train_all_data = np.concatenate((train_all_data, temp1), axis=0)
            train_all_label = np.concatenate((train_all_label, temp2), axis=0)
            random_indices = np.random.permutation(train_all_data.shape[0])
            train_all_data, train_all_label = train_all_data[
                random_indices], train_all_label[random_indices]
        else:
            temp1 = np.load(f"./pre-test/change_header/Data-{name}.npy",
                            allow_pickle=True)
            temp2 = np.load(f"./pre-test/change_header/Label-{name}.npy",
                            allow_pickle=True)
            test_all_data = np.concatenate((test_all_data, temp1), axis=0)
            test_all_label = np.concatenate((test_all_label, temp2), axis=0)
            random_indices = np.random.permutation(test_all_data.shape[0])
            test_all_data, test_all_label = test_all_data[
                random_indices], test_all_label[random_indices]
    return train_all_data, train_all_label, test_all_data, test_all_label


def save_all_npy(train_all_data, train_all_label, test_all_data,
                 test_all_label, method):
    np.save(f"./pre-train/Data-All-{method}.npy", train_all_data)
    np.save(f"./pre-train/Label-All-{method}.npy",
            train_all_label.astype(np.int))
    np.save(f"./pre-test/Data-All-{method}.npy", test_all_data)
    np.save(f"./pre-test/Label-All-{method}.npy",
            test_all_label.astype(np.int))


if __name__ == '__main__':
    data_sets = creat_data_sets(None, 9000, 13000, 1000, "Default")
    save_to_npy(data_sets.final_data_sets, 'change_header')
    train_all_data, train_all_label, test_all_data, test_all_label = concatenate_npy(
        data_sets.first_path)
    save_all_npy(train_all_data, train_all_label, test_all_data,
                 test_all_label, 'change_header')
