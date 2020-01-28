U = [10 15 1;8 3 1;11 17 1;5 11 1;6 13 1]
X = [33 20 1;18 7 1;37 22 1;20 13 1;23 16 1]
T = inv(U'*U)*U'*X

% Transformation
input_image = imread('cameraman.tif')
name="original_to_tranformed_img.tif"
trans(input_image,T,name)

% Inverse Transformation
input_image = imread('original_to_tranformed_img.tif')
name="tranformed_img_to_original.tif"
trans(input_image,T,name)