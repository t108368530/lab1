# 實驗報告(語音者識別)

- [實驗報告](#實驗報告語音者識別) 
  - [說明](#說明)
  - [腳本示意圖](#腳本示意圖)
  - [結果](#結果)
  - [心得觀察討論](#心得觀察討論)
  - [其他變聲方法](#其他變聲方法)

---

### 說明

1. 實驗主題
   - 語音者識別
2. 實驗資料
   - 來源：教授所給的資料集(學長所錄音的)
   - 語者數量：10個
   - 檔案數量：400筆(每個語者40筆資料)
3. 實驗環境(是使用Anaconda)
   - OS:Ubunut20.04
   - Language:Python(Version 3.8.1)
   - IDE:JupyterLab
4. 簡易步驟
   - 分切資料 -> 特徵取樣 -> 創建模型 -> 訓練模型 -> 測試模型

- 資料集組成
  - 訓練資料 = 訓練資料夾內音檔(沒調音)+訓練資料夾內音檔(調音方法(Librosa(pitch_shift) or TD-Psola)
  - 驗證資料 = 驗證資料夾內音檔(沒調音)
  - 測試資料 = 調音資料夾內音檔(調音方法(Librosa(pitch_shift) or TD-Psola,此資料不包含在訓練資料裡面)

---

### 腳本示意圖

1. 資料切割
   ![](https://i.imgur.com/HJupvJr.png)
   
2. 特徵取樣
   ![](https://i.imgur.com/8bgkPSV.png)
   
3. [Github(整個實驗放置處)](https://github.com/t108368530/lab1)

---

### 結果
- 表一. 訓練資料使用librosa 的 pitch_shift 提高1-7個音階做資料增廣，驗證資料(無調音),測試資料(固定調音高8)，優化器(Stochastic Gradient Descent; SGD)

|  Model  |         訓練參數          | 驗證資料(Valid)正確率 | 測試資料(Test)正確率 |
|:-------:|:-------------------------:|:-----------------:|:----------------:|
| **MLP** | epochs=200,batch_size=128 |        85%        |       91%        |
| **CNN** | epochs=25,batch_size=128  |        70%        |       91%        |


- 表二. 訓練資料使用TD-Psola調音，調整比率為 $2^{(\frac{i}{12})}，i為1到12$，驗證資料(無調音),測試資料(固定調音比率為$2^{(\frac{i}{12})} ,i為12$)，優化器SGD

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        95%        |       95%        |   0.1378   |
| **CNN** | epochs=25,batch_size=128  |        95%        |       95%        |   0.1006   |

- 表三. 訓練資料使用TD-Psola調音，調整比率為 $2^{(\frac{i}{12})}，i為1到12$，驗證資料(無調音),測試資料(固定調音比率為$2^{(\frac{i}{12})} ,i為16$)，優化器(Adaptive Moment Estimation; Adam)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        95%        |       74%        |   0.833    |
| **CNN** | epochs=25,batch_size=128  |        98%        |       77%        |   1.2630   |

:::info
以下表格的實驗，測試資料是經過Morphvox Pro軟體變聲的，表四至六分別是使用該軟體套至不同的變聲配置檔案作為測試資料來源，所做出的結果。
Morphvox Pro是google就會直接找到的常用變聲軟體
:::

- 表四. 訓練資料使用TD-Psola調音，調整比率為 $2^{(\frac{i}{12})}，i為1到12$，驗證資料(無調音),測試資料(使用Morphvox Pro做調音-配置檔案1)，優化器(Adaptive Moment Estimation; Adam)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        95%        |       47%        |   2.0956  |
| **CNN** | epochs=25,batch_size=128  |        95%        |       54%        |   2.2901   |

- 表五. 訓練資料使用TD-Psola調音，調整比率為 $2^{(\frac{i}{12})}，i為1到12$，驗證資料(無調音),測試資料(使用Morphvox Pro做調音-配置檔案2)，優化器(Adaptive Moment Estimation; Adam)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        93%        |       52%        |   1.7243    |
| **CNN** | epochs=25,batch_size=128  |        98%        |       48%        |   2.2583  |

- 表六. 訓練資料使用TD-Psola調音，調整比率為 $2^{(\frac{i}{12})}，i為1到12$，驗證資料(無調音),測試資料(使用Morphvox Pro做調音-配置檔案3)，優化器(Adaptive Moment Estimation; Adam)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        93%        |       41%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        98%        |       43%        |  2.6741   |


:::info
以下表格
訓練資料變音方式：Librosa
驗證資料變音方式：沒有進行變音
測試資料變音方式分別為：Librosa,Morphvox_Pro,TD-PSOLA
測試 Librosa 變音參數：3
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案
測試 TD-PSOLA 變音參數：固定調音比率為$2^{(\frac{i}{12})} ,i為18$
:::

- 表七. 測試資料變音方式經由Librosa變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        80%        |       87%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        73%        |       88%        |  2.6741   |

- 表八. 測試資料變音方式經由Morphvox_Pro變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        80%        |       26%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        73%        |       20%        |  2.6741   |

- 表九. 測試資料變音方式經由TD-PSOLA變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        80%        |       49%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        73%        |       50%        |  2.6741   |

:::info
以下表格
訓練資料變音方式：Morphvox_Pro
驗證資料變音方式：沒有進行變音
測試資料變音方式分別為：Librosa,Morphvox_Pro,TD-PSOLA
測試 Librosa 變音參數：3
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案
測試 TD-PSOLA 變音參數：固定調音比率為$2^{(\frac{i}{12})} ,i為18$
:::

- 表十. 測試資料變音方式經由Librosa變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        28%        |       30%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        30%        |       31%        |  2.6741   |

- 表十一. 測試資料變音方式經由Morphvox_Pro變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        24%        |       86%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        27%        |       88%        |  2.6741   |

- 表十二. 測試資料變音方式經由TD-PSOLA變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        24%        |       43%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        27%        |       48%        |  2.6741   |

:::info
以下表格
訓練資料變音方式：TD-PSOLA
驗證資料變音方式：沒有進行變音
測試資料變音方式分別為：Librosa,Morphvox_Pro,TD-PSOLA
測試 Librosa 變音參數：3
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案
測試 TD-PSOLA 變音參數：固定調音比率為$2^{(\frac{i}{12})} ,i為18$
:::

- 表十三. 測試資料變音方式經由Librosa變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        28%        |       30%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        30%        |       31%        |  2.6741   |

- 表十四. 測試資料變音方式經由Morphvox_Pro變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        94%        |       27%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        98%        |       25%        |  2.6741   |

- 表十五. 測試資料變音方式經由TD-PSOLA變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=200,batch_size=128 |        94%        |       83%        |   2.8149    |
| **CNN** | epochs=25,batch_size=128  |        98%        |       84%        |  2.6741   |

:::info
以下表格
訓練資料變音方式包含：Librosa,Morphvox_Pro,TD-PSOLA
驗證資料變音方式：沒有進行變音
測試資料變音方式包含：Librosa,Morphvox_Pro,TD-PSOLA
測試 Librosa 變音參數：3
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案
測試 TD-PSOLA 變音參數：固定調音比率為$2^{(\frac{i}{12})} ,i為18$
:::
- 表十六. 測試資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        89%        |       80%        |   1.4656    |
| **CNN** | epochs=200,batch_size=128  |        81%        |       81%        |  1.0239   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/zXWEYcd.png) | ![](https://i.imgur.com/GiEEE0R.png) |



- 表十七. 測試資料變音方式經由Librosa變音 

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        94%        |       71%        |  2.3621    |
| **CNN** | epochs=200,batch_size=128  |        81%        |       76%        |  1.2373   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/ExfPofS.png) |![](https://i.imgur.com/61JFJki.png)|

- 表十八. 測試資料變音方式經由Morphvox_Pro變音 

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        94%        |       75%        |  1.2397    |
| **CNN** | epochs=200,batch_size=128  |        81%        |       81%        |  0.8540   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/pRidXMn.png)|![](https://i.imgur.com/agtR4Uq.png)
|


- 表十九. 測試資料變音方式經由TD-PSOLA變音 


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        94%        |       78%        |   2.1972    |
| **CNN** | epochs=200,batch_size=128  |        81%        |       74%        |  1.1798   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/CuCKwDu.png) | ![](https://i.imgur.com/GH31yX9.png)|

:::info
以下表格
訓練資料變音方式包含：Librosa,Morphvox_Pro,TD-PSOLA
驗證資料變音方式：沒有進行變音
測試資料變音方式包含：Librosa,Morphvox_Pro,TD-PSOLA
測試 Librosa 變音參數：3
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案
測試 TD-PSOLA 變音參數：固定調音比率為$2^{(\frac{i}{12})} ,i為18$
取樣頻率：32000 ,44100 ,48000 ,50000 ,96000
:::

- 表二十. 測試與訓練資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音,取樣頻率為32000


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        78%        |       77%        |   1.4361   |
| **CNN** | epochs=500,batch_size=128  |        79%        |       78%        |  1.1878   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/XrGC1V3.png)| ![](https://i.imgur.com/P1oS3Qv.png)|

- 表二十一. 測試與訓練資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音,取樣頻率為44100


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        81%        |       78%        |   1.1370   |
| **CNN** | epochs=500,batch_size=128  |        70%        |       80%        |  1.0916   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/LrgvCpg.png)| ![](https://i.imgur.com/p6zNhLs.png)|

- 表二十二. 測試與訓練資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音,取樣頻率為48000


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        71%        |       78%        |   1.1370   |
| **CNN** | epochs=500,batch_size=128  |        64%        |       79%        |  1.1120   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/ZMTkFVR.png)| ![](https://i.imgur.com/RWMcEZb.png)|

- 表二十三. 測試與訓練資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音,取樣頻率為50000


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        71%        |       78%        |  1.5337  |
| **CNN** | epochs=500,batch_size=128  |        66%        |       79%        |  1.1120   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/Q2j6g4K.png)| ![](https://i.imgur.com/9N0l0Rg.png)|

- 表二十四. 測試與訓練資料變音方式包含Librosa,Morphvox_Pro,TD-PSOLA變音,取樣頻率為96000


|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        27%        |       77%        |  1.5337  |
| **CNN** | epochs=500,batch_size=128  |        36%        |       76%        |  1.2198   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** | ![](https://i.imgur.com/wqPlQea.png)| ![](https://i.imgur.com/ksDqLkQ.png)|

:::info  
以下表格: 
更換檔案標頭取樣頻率為：9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz 
驗證資料變音方式：沒有進行變音  
測試 Librosa 變音參數：3  
測試 Morphvox_Pro 變音參數：4種該程式變音設定檔案  
測試 TD-PSOLA 變音參數：固定調音比率為 $2^{(\frac{i}{12})} ,i為18$ 
- 訓練資料調整方式分為兩種：  
  1. Librosa,Morphvox_Pro,TD-PSOLA  
  2. Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)  
- 測試資料：  
  1. 更換檔案標頭的音檔特徵(個別測試)  
:::

- 表二十五. 
  - 測試資料取樣頻率為：9000Hz
  - 訓練資料為包含:Librosa,Morphvox_Pro,TD-PSOLA
 
|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        80%        |       33%        |  4.9892  |
| **CNN** | epochs=500,batch_size=128  |        81%        |       37%        | 4.0315   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/hqp5AUc.png)|![](https://i.imgur.com/Mcq5n3A.png)|


- 表二十六. 
  - 測試資料取樣頻率為：10000Hz 
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        80%        |       27%        |  5.2229  |
| **CNN** | epochs=500,batch_size=128  |        81%        |       30%        | 4.5645   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/S735Cc1.png)|![](https://i.imgur.com/2kTHaNY.png)|

- 表二十七. 
  - 測試資料取樣頻率為：11000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        80%        |       23%        |  5.3145  |
| **CNN** | epochs=500,batch_size=128  |        81%        |       23%        | 5.1518   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/GFdP8To.png)|![](https://i.imgur.com/xuksYhI.png)|

表二十八. 
測試資料取樣頻率為：12000Hz
訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA
|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        80%        |       23%        |  5.2868  |
| **CNN** | epochs=500,batch_size=128  |        81%        |       23%        | 5.3706   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/uCpcC99.png)|![](https://i.imgur.com/rXF0bSz.png)|

- 表二十九. 
  - 測試資料取樣頻率為：13000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        80%        |       31%        |  4.8962  |
| **CNN** | epochs=500,batch_size=128  |        81%        |       20%        | 5.3173   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/Lk9KYIL.png)|![](https://i.imgur.com/EN7K75D.png)|

- 表三十. 
  - 測試資料取樣頻率為：9000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       88%        |  0.5127  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       82%        | 0.8361   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/i7z3vgJ.png)|![](https://i.imgur.com/GSXTNhM.png)|

- 表三十一. 
  - 測試資料取樣頻率為：10000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)
  
|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       88%        |  0.6850  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       86%        | 0.7106   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/Afmut81.png)|![](https://i.imgur.com/Z01QwWX.png)|

- 表三十二. 
  - 測試資料取樣頻率為：11000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       87%        |  0.7774  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       82%        | 0.7950   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/hmjEEYQ.png)|![](https://i.imgur.com/yM2G5p2.png)|

- 表三十三. 
  - 測試資料取樣頻率為：12000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       88%        |  0.7774  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       82%        | 0.7950   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/P0fm868.png)|![](https://i.imgur.com/WnFKSoa.png)|

- 表三十四. 
  - 測試資料取樣頻率為：13000Hz
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       81%        |  1.0061  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       82%        | 0.9397   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/ad8IqNU.png)|![](https://i.imgur.com/P9hIkiq.png)|

- 表三十五. 
  - 測試資料取樣頻率為：12500Hz 
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       81%        |  1.0061  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       81%        | 0.8384   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/g9zNhR1.png)|![](https://i.imgur.com/7x6N6fS.png)|

- 表三十六. 
  - 測試資料取樣頻率為：14000Hz 
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |         訓練參數          | Valid Data 正確率 | Test Data 正確率 | Loss(Test) |
|:-------:|:-------------------------:|:-----------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |        86%        |       68%        |  1.6706  |
| **CNN** | epochs=500,batch_size=128  |        89%        |       75%        | 1.4053   |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://i.imgur.com/L2KgeGh.png)|![](https://i.imgur.com/cFt0ATU.png)|

:::info
表.37 至 69: [訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)]
表.70 至 114:[訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz-48000Hz)
:::

- 表三十七. 
  - 測試資料取樣頻率為：16000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       37%        |   4.0292  |
| **CNN** | epochs=500,batch_size=128  |       50%        |   2.6536    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_16000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_16000.png)|


- 表三十八. 
  - 測試資料取樣頻率為：17000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       30%        |   4.8122  |
| **CNN** | epochs=500,batch_size=128  |       44%        |   3.0972    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_17000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_17000.png)|


- 表三十九. 
  - 測試資料取樣頻率為：18000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       28%        |   5.0634  |
| **CNN** | epochs=500,batch_size=128  |       37%        |   3.4861    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_18000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_18000.png)|


- 表四十. 
  - 測試資料取樣頻率為：19000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       27%        |   5.4267  |
| **CNN** | epochs=500,batch_size=128  |       31%        |   3.7576    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_19000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_19000.png)|


- 表四十一. 
  - 測試資料取樣頻率為：20000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       21%        |   5.9869  |
| **CNN** | epochs=500,batch_size=128  |       28%        |   4.0763    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_20000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_20000.png)|


- 表四十二. 
  - 測試資料取樣頻率為：21000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   6.4819  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   4.5064    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_21000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_21000.png)|


- 表四十三. 
  - 測試資料取樣頻率為：22000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       21%        |   6.8034  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   4.7212    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_22000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_22000.png)|


- 表四十四. 
  - 測試資料取樣頻率為：23000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   6.0839  |
| **CNN** | epochs=500,batch_size=128  |       27%        |   4.9660    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_23000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_23000.png)|


- 表四十五. 
  - 測試資料取樣頻率為：24000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       21%        |   5.5196  |
| **CNN** | epochs=500,batch_size=128  |       27%        |   5.1530    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_24000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_24000.png)|


- 表四十六. 
  - 測試資料取樣頻率為：25000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   5.8123  |
| **CNN** | epochs=500,batch_size=128  |       31%        |   5.3079    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_25000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_25000.png)|


- 表四十七. 
  - 測試資料取樣頻率為：26000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   5.8147  |
| **CNN** | epochs=500,batch_size=128  |       30%        |   5.3293    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_26000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_26000.png)|


- 表四十八. 
  - 測試資料取樣頻率為：27000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       15%        |   5.5153  |
| **CNN** | epochs=500,batch_size=128  |       31%        |   5.3289    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_27000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_27000.png)|


- 表四十九. 
  - 測試資料取樣頻率為：28000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       11%        |   5.4728  |
| **CNN** | epochs=500,batch_size=128  |       28%        |   5.3409    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_28000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_28000.png)|


- 表五十. 
  - 測試資料取樣頻率為：29000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       15%        |   5.2371  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   5.3875    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_29000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_29000.png)|


- 表五十一. 
  - 測試資料取樣頻率為：30000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       20%        |   5.2500  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   5.4569    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_30000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_30000.png)|


- 表五十二. 
  - 測試資料取樣頻率為：31000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       18%        |   5.1849  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   5.5484    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_31000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_31000.png)|


- 表五十三. 
  - 測試資料取樣頻率為：32000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       20%        |   5.2031  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   5.5907    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_32000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_32000.png)|


- 表五十四. 
  - 測試資料取樣頻率為：33000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       21%        |   5.3559  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   5.7710    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_33000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_33000.png)|


- 表五十五. 
  - 測試資料取樣頻率為：34000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   5.5379  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   5.7879    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_34000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_34000.png)|


- 表五十六. 
  - 測試資料取樣頻率為：35000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   5.7735  |
| **CNN** | epochs=500,batch_size=128  |       21%        |   6.0327    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_35000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_35000.png)|


- 表五十七. 
  - 測試資料取樣頻率為：36000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   6.0841  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   6.2763    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_36000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_36000.png)|


- 表五十八. 
  - 測試資料取樣頻率為：37000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   6.0915  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   6.5676    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_37000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_37000.png)|


- 表五十九. 
  - 測試資料取樣頻率為：38000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       27%        |   5.9170  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   6.7259    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_38000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_38000.png)|


- 表六十. 
  - 測試資料取樣頻率為：39000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   6.0515  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   6.8353    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_39000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_39000.png)|


- 表六十一. 
  - 測試資料取樣頻率為：40000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   6.5168  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   6.9172    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_40000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_40000.png)|


- 表六十二. 
  - 測試資料取樣頻率為：41000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       21%        |   6.7396  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   6.9300    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_41000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_41000.png)|


- 表六十三. 
  - 測試資料取樣頻率為：42000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       25%        |   6.7469  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   6.9905    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_42000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_42000.png)|


- 表六十四. 
  - 測試資料取樣頻率為：43000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   6.5194  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   6.8640    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_43000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_43000.png)|


- 表六十五. 
  - 測試資料取樣頻率為：44000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   6.4781  |
| **CNN** | epochs=500,batch_size=128  |       18%        |   6.8218    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_44000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_44000.png)|


- 表六十六. 
  - 測試資料取樣頻率為：45000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       20%        |   6.4697  |
| **CNN** | epochs=500,batch_size=128  |       20%        |   6.7690    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_45000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_45000.png)|


- 表六十七. 
  - 測試資料取樣頻率為：46000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       23%        |   6.5560  |
| **CNN** | epochs=500,batch_size=128  |       21%        |   6.5908    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_46000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_46000.png)|


- 表六十八. 
  - 測試資料取樣頻率為：47000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       20%        |   6.6532  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   6.4943    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_47000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_47000.png)|

- 表六十九. 
  - 測試資料取樣頻率為：48000
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(9000Hz ,10000Hz ,11000Hz ,12000Hz ,13000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       20%        |   6.7646  |
| **CNN** | epochs=500,batch_size=128  |       25%        |   6.4640    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/mlp_48000.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/1/cnn_48000.png)|


- 表七十. 
  - 測試資料取樣頻率為：4500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       83%        |   0.9381  |
| **CNN** | epochs=500,batch_size=128  |       72%        |   0.8110    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_4500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_4500.png)|


- 表七十一. 
  - 測試資料取樣頻率為：5500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       83%        |   1.2865  |
| **CNN** | epochs=500,batch_size=128  |       70%        |   0.8769    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_5500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_5500.png)|


- 表七十二. 
  - 測試資料取樣頻率為：6500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   1.3993  |
| **CNN** | epochs=500,batch_size=128  |       75%        |   0.9188    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_6500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_6500.png)|


- 表七十三. 
  - 測試資料取樣頻率為：7500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   1.2623  |
| **CNN** | epochs=500,batch_size=128  |       72%        |   0.9083    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_7500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_7500.png)|


- 表七十四. 
  - 測試資料取樣頻率為：8500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       85%        |   0.9879  |
| **CNN** | epochs=500,batch_size=128  |       68%        |   0.9669    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_8500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_8500.png)|


- 表七十五. 
  - 測試資料取樣頻率為：9500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   0.8998  |
| **CNN** | epochs=500,batch_size=128  |       75%        |   0.9320    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_9500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_9500.png)|


- 表七十六. 
  - 測試資料取樣頻率為：10500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.1138  |
| **CNN** | epochs=500,batch_size=128  |       69%        |   0.9455    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_10500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_10500.png)|


- 表七十七. 
  - 測試資料取樣頻率為：11500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.1451  |
| **CNN** | epochs=500,batch_size=128  |       73%        |   0.9553    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_11500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_11500.png)|


- 表七十八. 
  - 測試資料取樣頻率為：12500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.2852  |
| **CNN** | epochs=500,batch_size=128  |       69%        |   1.0193    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_12500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_12500.png)|


- 表七十九. 
  - 測試資料取樣頻率為：13500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.4501  |
| **CNN** | epochs=500,batch_size=128  |       69%        |   0.9608    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_13500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_13500.png)|


- 表八十. 
  - 測試資料取樣頻率為：14500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       77%        |   1.5191  |
| **CNN** | epochs=500,batch_size=128  |       74%        |   0.8880    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_14500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_14500.png)|


- 表八十一. 
  - 測試資料取樣頻率為：15500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.4912  |
| **CNN** | epochs=500,batch_size=128  |       76%        |   0.9213    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_15500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_15500.png)|


- 表八十二. 
  - 測試資料取樣頻率為：16500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       83%        |   1.6008  |
| **CNN** | epochs=500,batch_size=128  |       75%        |   0.8889    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_16500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_16500.png)|


- 表八十三. 
  - 測試資料取樣頻率為：17500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       77%        |   1.7229  |
| **CNN** | epochs=500,batch_size=128  |       76%        |   0.8872    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_17500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_17500.png)|


- 表八十四. 
  - 測試資料取樣頻率為：18500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.5849  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.8823    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_18500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_18500.png)|


- 表八十五. 
  - 測試資料取樣頻率為：19500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       77%        |   1.4847  |
| **CNN** | epochs=500,batch_size=128  |       75%        |   0.9403    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_19500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_19500.png)|


- 表八十六. 
  - 測試資料取樣頻率為：20500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       75%        |   1.5663  |
| **CNN** | epochs=500,batch_size=128  |       77%        |   0.8730    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_20500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_20500.png)|


- 表八十七. 
  - 測試資料取樣頻率為：21500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       74%        |   1.7625  |
| **CNN** | epochs=500,batch_size=128  |       77%        |   0.8782    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_21500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_21500.png)|


- 表八十八. 
  - 測試資料取樣頻率為：22500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       75%        |   1.6928  |
| **CNN** | epochs=500,batch_size=128  |       79%        |   0.8326    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_22500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_22500.png)|


- 表八十九. 
  - 測試資料取樣頻率為：23500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       80%        |   1.5956  |
| **CNN** | epochs=500,batch_size=128  |       77%        |   0.8079    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_23500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_23500.png)|


- 表九十. 
  - 測試資料取樣頻率為：24500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.5952  |
| **CNN** | epochs=500,batch_size=128  |       76%        |   0.8561    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_24500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_24500.png)|


- 表九十一. 
  - 測試資料取樣頻率為：25500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.7155  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.8521    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_25500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_25500.png)|


- 表九十二. 
  - 測試資料取樣頻率為：26500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       77%        |   1.5166  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.8658    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_26500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_26500.png)|


- 表九十三. 
  - 測試資料取樣頻率為：27500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.6912  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.8115    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_27500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_27500.png)|


- 表九十四. 
  - 測試資料取樣頻率為：28500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       80%        |   1.7779  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.8011    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_28500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_28500.png)|


- 表九十五. 
  - 測試資料取樣頻率為：29500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       79%        |   1.8028  |
| **CNN** | epochs=500,batch_size=128  |       76%        |   0.7739    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_29500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_29500.png)|


- 表九十六. 
  - 測試資料取樣頻率為：30500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.7012  |
| **CNN** | epochs=500,batch_size=128  |       79%        |   0.7370    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_30500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_30500.png)|


- 表九十七. 
  - 測試資料取樣頻率為：31500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.6233  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.7013    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_31500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_31500.png)|


- 表九十八. 
  - 測試資料取樣頻率為：32500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.5226  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.6679    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_32500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_32500.png)|


- 表九十九. 
  - 測試資料取樣頻率為：33500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   1.6489  |
| **CNN** | epochs=500,batch_size=128  |       79%        |   0.6581    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_33500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_33500.png)|


- 表一百. 
  - 測試資料取樣頻率為：34500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   1.5596  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.6570    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_34500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_34500.png)|


- 表一百○一. 
  - 測試資料取樣頻率為：35500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.5913  |
| **CNN** | epochs=500,batch_size=128  |       85%        |   0.6743    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_35500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_35500.png)|


- 表一百○二. 
  - 測試資料取樣頻率為：36500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       83%        |   1.5319  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.6655    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_36500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_36500.png)|


- 表一百○三. 
  - 測試資料取樣頻率為：37500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.4848  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.6829    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_37500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_37500.png)|


- 表一百○四. 
  - 測試資料取樣頻率為：38500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.3939  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.6620    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_38500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_38500.png)|


- 表一百○五. 
  - 測試資料取樣頻率為：39500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       86%        |   1.3362  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.7125    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_39500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_39500.png)|


- 表一百○六. 
  - 測試資料取樣頻率為：40500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       86%        |   1.3474  |
| **CNN** | epochs=500,batch_size=128  |       79%        |   0.6759    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_40500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_40500.png)|


- 表一百○七. 
  - 測試資料取樣頻率為：41500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       83%        |   1.5060  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.6484    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_41500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_41500.png)|


- 表一百○八. 
  - 測試資料取樣頻率為：42500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       82%        |   1.5696  |
| **CNN** | epochs=500,batch_size=128  |       83%        |   0.6858    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_42500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_42500.png)|


- 表一百○九. 
  - 測試資料取樣頻率為：43500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       81%        |   1.5896  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.6997    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_43500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_43500.png)|


- 表一百一十. 
  - 測試資料取樣頻率為：44500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       77%        |   1.6224  |
| **CNN** | epochs=500,batch_size=128  |       82%        |   0.7385    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_44500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_44500.png)|


- 表一百一十一. 
  - 測試資料取樣頻率為：45500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       80%        |   1.6003  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.7150    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_45500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_45500.png)|


- 表一百一十二. 
  - 測試資料取樣頻率為：46500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       76%        |   1.6774  |
| **CNN** | epochs=500,batch_size=128  |       81%        |   0.7319    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_46500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_46500.png)|


- 表一百一十三. 
  - 測試資料取樣頻率為：47500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       74%        |   1.8399  |
| **CNN** | epochs=500,batch_size=128  |       80%        |   0.7748    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_47500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_47500.png)|


- 表一百一十四. 
  - 測試資料取樣頻率為：48500
  - 訓練資料為包含：Librosa,Morphvox_Pro,TD-PSOLA,資料取樣頻率為(4000Hz - 48000Hz)

|  Model  |          訓練參數          | Test Data 正確率 | Loss(Test) |
|:-------:|:--------------------------:|:----------------:|:----------:|
| **MLP** | epochs=1000,batch_size=128 |       73%        |   1.9111  |
| **CNN** | epochs=500,batch_size=128  |       79%        |   0.7754    |

|      Model       |               **MLP**                |               **CNN**                |
|:----------------:|:------------------------------------:|:------------------------------------:|
| **Comfusion Matrix** |![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/mlp_48500.png)|![](https://raw.githubusercontent.com/t108368530/lab1/master/img/3/cnn_48500.png)|






### 心得,觀察,討論

- 心得
  - 剛開始在看學長的留下來的code，特徵提取方面是使用不同音訊特徵提取方法，再將特徵展平，然後將其餵入類神經網路內，再利用資料增廣(調整音訊的音調與音階)前，正確率大約只有70%左右，之後有明顯提升至91%。 
  - 數據增強使用TD-Psola方式調音，在[結果](#結果)TD-Psola方式調音顯示會比使用Librosa 的 Pitch_Shift 來做數據增強來的準
  - 音訊檔案在更改標頭後，在做一樣的特徵擷取時候，調用"頻譜對比值"的時候有發生，Nyquist frequency會混疊的問題，一剛開始我是將取樣的頻帶數從6調整到到5解決這個問題，但後來把全部的特徵值和時候，特徵值與前幾次取出來的有所差，所以後來是調整最小取樣頻率來解決的。**(更新於 2020/09/30)**




- 觀察 
  - 特徵提取時MFCC特徵，經過算數平均數的計算因此重要訊息被壓縮到了
  - 在此網絡最高的正確率就是91％，可能需要調整網絡架構
  - 提取太多特徵，提取速度較慢
  - 從[結果](#結果)表四到六，發現準確率有明顯下降 **(更新於 2020/08/09)**
  - 測試資料集取樣頻率超過訓練資料集取樣頻率就會開始下降
  - 如果資料集是模型所沒看過的，那在做預估時候效果會很差 **(更新於 2020/09/30)**

- 討論
  - 小波轉換取特徵可能會更好，因為低通濾波器，可以將輸入訊號的高頻部份濾掉而輸出低頻部份,高通濾波器，可以將輸入訊號的低頻部份濾掉而輸出高頻部份。
  - 如果優化Loss Function,使整個網絡再調整全中有所差異
  - 我有在做一個小實驗使用TD-Psola方式對測試資料集調音，調整比率為 $2^{(\frac{i}{1６})}，i為16$，此時的測試資料調音範圍是超出訓練資料集的調音範圍，從[結果](#結果)中的表三可看出正確率有明顯下降
  - 從[結果](#結果)中的表三到六，可以發現只要超過訓練資料及的範圍，模型的準確率，會有明顯的下降，我要嘗試把提取特徵的方法做更改，還有模型也做更改，特徵提取改用mel spectrogra或MFCC， 模型改用２維卷積與 **(更新於 2020/08/09)**
  - 
 
  
  
  
