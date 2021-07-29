<div align="center">    
 
# NTable: A Dataset for Camera-based Table Detection 

</div>

Most of the existing table detection methods are designed for scanned document images or Portable Document Format (PDF). And tables in the real world are seldom collected in the current mainstream table detection datasets. Therefore, we construct a dataset named NTable for camera-based table detection. NTable consists of a smaller-scale dateset NTable-ori, an augmented dataset NTable-cam, and a generated dataset NTable-gen. More details are available in our paper "NTable: A Dataset for Camera-based Table Detection".

## Description
**NTable-ori** is made up of 2.1k+ images taken by different cameras and mobile phones. We provide two classification methods, one is based on the source, the other is based on the shape (see Examples). According to the source, NTable-ori can be divided into textual, electronic and wild. According to the shape, NTable-ori can be divided into upright, oblique and distorted. Table 1 counts the classification results.
 
<div align="center">
Table 1. Classification results of NTable-ori.
</div>
<table align="center">
   <tr>
      <td>category </td>
      <td colspan = "3" align="center">source </td>
      <td colspan = "3" align="center">shape</td>
   </tr>
   <tr>
      <td> subcategory </td>
      <td> textual </td>
      <td> electronic </td>
      <td> wild </td>
      <td> upright </td>
      <td> oblique </td>
      <td>distorted </td>
   </tr>
   <tr align="center">
      <td># of pages </td>
      <td>1674</td>
      <td>254</td>
      <td>198</td>
      <td>758</td>
      <td>421</td>
      <td>947</td>
   </tr>
</table>
 
**NTable-cam** is augmented from NTable-ori. By changing rotation, brightness and contrast, original 2.1k+ images are expanded eightfold to 17k+ images (see Examples).
 
**NTable-gen** is a synthetic dataset, it simulates as much as possible the various deformation conditions, which is to address the limitations of the current data, ulteriorly improve data richness. We chose [PubLayNet](https://github.com/ibm-aur-nlp/PubLayNet) as the original document images. There are 86950 pages with at least one table in PubLayNet’s training set. We randomly select 8750 pages. Background images are from the [VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/) dataset (see Examples).


## Get data
NTable-gen:
Link 1 (Google Drive), Link 2 (Baidu Disk)
 
The original NTable-ori and NTable-cam:
Link 1 (Google Drive), Link 2 (Baidu Disk)
 
We collected 607 new images, including 1000 tables. The statistics are shown in Table 2. Download link：
Link 1 (Google Drive), Link 2 (Baidu Disk)
 
<div align="center">
Table 2. Classification results of the new images.
</div>
<table align="center">
   <tr>
      <td>category </td>
      <td colspan = "3" align="center">source </td>
      <td colspan = "3" align="center">shape</td>
   </tr>
   <tr>
      <td> subcategory </td>
      <td> textual </td>
      <td> electronic </td>
      <td> wild </td>
      <td> upright </td>
      <td> oblique </td>
      <td>distorted </td>
   </tr>
   <tr align="center">
      <td># of pages </td>
      <td>1674</td>
      <td>254</td>
      <td>198</td>
      <td>758</td>
      <td>421</td>
      <td>947</td>
   </tr>
</table>
 
## Annotation format
The annotation files follows the format of YOLO, [x, y, w, h] determines a bounding box, (x, y) is the coordinate of the center of the bounding box, w and h is the normalized width and height of the bounding box, where w is $$\frac{width of the bbox}{width of the image}$$,  h is $$\frac{height of the bbox}{height of the image}$$. 
  
![](http://latex.codecogs.com/gif.latex?\\sigma=\sqrt{\frac{1}{n}{\sum_{k=1}^n(x_i-\bar{x})^2}})
 
 
## Examples

## Note
1. This classification is 主观的, 例如 you may find some 被分类为upright的 tables 有一些轻微的变形或倾斜
2. 我们的论文中的表格出现了一些笔误, 以下为正确表格:
3. 


## Acknowledgement
