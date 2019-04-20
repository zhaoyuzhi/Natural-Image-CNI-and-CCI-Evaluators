# Natural-Image-CNI-and-CCI-Evaluators

## 1 CNI

CNI is known as `Color Naturalness Index`, which is a kind of `no reference evaluator`.
</br>
To compute CNI, `first step` is transferring the given image to `HSL color space`.
</br>
The `second step` is `computing the H, S, L values of each pixel`, and `classifying them pixel by pixel` as follows:
</br>
Retain the pixels whose `S > 1` and `0.2 < L < 0.8`, delete other pixels which are not eligible
</br>
`Class 1: 25 <= H <= 70`, which is named as `skin pixel`, then `save the S value` of this pixel
</br>
`Class 2: 95 <= H <= 135`, which is named as `grass pixel`, then `save the S value` of this pixel
</br>
`Class 3: 185 <= H <= 260`, which is named as `sky pixel`, then `save the S value` of this pixel
</br>
The `third step` is `computing the average values for each kinds of pixels` (skin, grass, and sky)
</br>
The `fourth step` is `computing local CNI values`, given as follows:
</br>
`temp_skin = (mean_skin - 0.76) / 0.52`
</br>
`N_skin = math.exp(- 0.5 * math.pow(temp, 2))`
</br>
`temp_grass = (mean_skin - 0.81) / 0.53`
</br>
`N_grass = math.exp(- 0.5 * math.pow(temp, 2))`
</br>
`temp_sky = (mean_skin - 0.43) / 0.22`
</br>
`N_sky = math.exp(- 0.5 * math.pow(temp, 2))`
</br>
The `final step` is `computing the global CNI value`, given as follows:
</br>
`if (len(skin) + len(grass) + len(sky)) == 0: N = 0`
</br>
`else: N = len(skin) * N_skin + len(grass) * N_grass + len(sky) * N_sky / len(skin) + len(grass) + len(sky)`
</br>
`N` is the final `CNI` value.

## 2 CCI

CCI is known as `Color Colorfulness Index`, which is also a kind of `no reference evaluator`.
</br>
First, compute the matrix `RG` and `YB`:
</br>
`RG = R - G`
</br>
`YB = 0.5 * R + 0.5 * G - B`
</br>
Then, compute the `CCI value`:
</br>
`mean = sqrt(RG_mean ^ 2 + YB_mean ^ 2)`
</br>
`std = sqrt(RG_std ^ 2 + YB_std ^ 2)`
</br>
`M = 0.3 * mean + std`
</br>
If `16 <= M <= 20`, the CCI value is visually good, while `M` is the final `CCI` output.

## 3 Reference
Kai-Qi Huang, Qiao Wang, and Zhen-Yang Wu. Natural color image enhancement and evaluation algorithm based on human visual system. Computer Vision and Image Understanding (CVIU), 2006, 103(1): 52-63.
