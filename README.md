# GoogleFontsDownloader

A simple Python script to download a font with all the styles, see the variants of each one, download a specific variant of the font or get the CSS import url

* The script does not include a API key by default. If you want to add it, just add to the the `api_key` variable your own API key. You can obtain an API key [here](https://console.cloud.google.com/marketplace/product/google/webfonts.googleapis.com)

## <ins>Install

1. Download the GitHub repository
2. Install the requeriments (`pip install -r requirements.txt`)
3. Run the script (`python3 GoogleFontsDownloader.py [OPTIONS]`)

## <ins>Options

```
usage: GoogleFontsDownloader.py [-h] [-f FONT] [-t TYPE] [-v] [-css]  

optional arguments:  
-h, --help show this help message and exit  
-f FONT, --font FONT Set the font name  
-t TYPE, --type TYPE Set the font type (regular, italic...)  
-v, --variants Get the variants of the font (-f)  
-css, --css Get the import CSS url
```

## <ins>Examples

#### Download a font (.zip)
`Syntax: python3 GoogleFontsDownloader.py -f FONT_NAME`
  
`Example: python3 GoogleFontsDownloader.py -f Roboto`
#### Get the font variants
`Syntax: python3 GoogleFontsDownloader.py -f FONT_NAME -v`
  
`Example: python3 GoogleFontsDownloader.py -f Roboto -v`
#### Download a font variant (.ttf)
`Syntax: python3 GoogleFontsDownloader.py -f FONT_NAME -t VARIANT`
  
`Example: python3 GoogleFontsDownloader.py -f Roboto -t 100italic`
#### Get the CSS import url
`Syntax: python3 GoogleFontsDownloader.py -f FONT_NAME -css`
  
`Example: python3 GoogleFontsDownloader.py -f Roboto -css`
