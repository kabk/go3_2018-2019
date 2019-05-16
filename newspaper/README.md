# HTML -> Print Newspaper

To generate the newspaper:

    $ python gen.py > index.html

Open the index.html file in a Webkit browser (ex. Google Chrome)

Right click -> Print

Save as pdf.

## Change the format

In template.html there is a css rule for the page size.

    @media print {
    @page {
      size: 262mm 372mm;
    }
    }

Note the javascript in template.html needs to know the height of the document.  The formula is in the comment.

    // 372 mm * 28 pages * 3.779528 px
    const h = 34605 

## Change the image or tag content

Look in gen.py at gen_images function.  There is an example on how to handle the sorting in the tagalytics function.  The tagalytics function is not otherwise used, note it is commented out in the bottom of gen.py.  It is only there to get information about the tags.

## Change out the layout works

Look at template.html, there is Javascript at the bottom.

## Content

There is a data directory/folder which should be next to the python script which is of the structure:

    data
     |_ IMAGE_TAGS
         |_ Article 1
              |_ image.png
              |_ foo.txt
              |_ image2.jpg
              |_ bar.txt
         |_ Article 2
         |_ ...

