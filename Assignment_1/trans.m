function x=trans(input_image,T,name)
    [rows,columns]=size(input_image)
    [X,Y] = meshgrid(0:columns-1,0:rows-1)
    ones_matrix = ones(rows,columns)
    
    original_coordinates = [X(:) Y(:) ones_matrix(:)] * inv(T)
    
    Xspecific = (original_coordinates(:,1))
    Yspecific = (original_coordinates(:,2))
    
    [X,Y] = meshgrid(0:columns-1,0:rows-1)
    out = griddata(X(:),Y(:),double(input_image(:)),Xspecific(:),Yspecific(:))
    output_image = reshape(out,rows,columns)

    imshow(output_image,[]) 
    %saving output image
    imwrite(output_image,name)
end