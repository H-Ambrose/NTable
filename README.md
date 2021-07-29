<div align="center">    
 
# NTable: A Dataset for Camera-based Table Detection 

</div>

Most of the existing table detection methods are designed for scanned document images or Portable Document Format (PDF). And tables in the real world are seldom collected in the current mainstream table detection datasets. Therefore, we construct a dataset named NTable for camera-based table detection. NTable consists of a smaller-scale dateset NTable-ori, an augmented dataset NTable-cam, and a generated dataset NTable-gen. More details are available in our paper "NTable: A Dataset for Camera-based Table Detection".

## Description
NTable-ori is made up of 2.1k+ images taken by different cameras and mobile phones. We provide two classification methods, one is based on the source, the other is based on the shape (see Examples). According to the source, NTable-ori can be divided into textual, electronic and wild. According to the shape, NTable-ori can be divided into upright, oblique and distorted. Table 1 counts the classification results.

<table>
   <tr>
      <td>category </td>
      <td>source </td>
      <td></td>
      <td></td>
      <td>shape</td>
      <td></td>
      <td></td>
   </tr>
   <tr>
      <td> subcategory </td>
      <td>textual </td>
      <td>electronic</td>
      <td> wild </td>
      <td>upright</td>
      <td> oblique </td>
      <td>distorted </td>
   </tr>
   <tr>
      <td># of pages </td>
      <td>1674</td>
      <td>254</td>
      <td>198</td>
      <td>758</td>
      <td>421</td>
      <td>947</td>
   </tr>
   <tr>
      <td></td>
   </tr>
</table>

## Get data

## Annotation format

## Examples

## Note
1. This classification is 主观的, 例如 you may find some 被分类为upright的 tables 有一些轻微的变形或倾斜
2. 我们的论文中的表格出现了一些笔误, 以下为正确表格:
3. 


## Acknowledgement
