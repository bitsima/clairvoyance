# Clairvoyance
A data extracting and validating web app. Extracts the data from images using Tesseract OCR.<br>
The app "extracts" the following types of data from images through regex, and then "validates" them (if applicable): <br>
```->phone numbers
->id numbers
->credit card numbers
->plate ids
->dates
->emails
->domains
->urls
->hashes
->combolists
```

The successful JSONResponse is of the form: <br>
```JSON/{
  "content": "This is a lot of 12 point text to test the\nocr code and see if it works on all types\nof file format.\n\nThe quick brown dog jumped over the\nlazy fox. The quick brown dog jumped\nover the lazy fox. The quick brown dog\njumped over the lazy fox. The quick\nbrown dog jumped over the lazy fox.",
  "status": "successful",
  "findings": [
    {
      "value": "12 point ",
      "type": "DATE"
    }
  ]
}
```

**TO RUN:**<br>
You need to have Docker installed on your machine. <br>
In order to run the containers, do: <br>
```docker compose up```

By default the app works on localhost:8000 and the url for the upload endpoint is ```http://localhost:8000/api/v1/upload/```. <br>
You can upload all image formats Tesseract OCR is compatible with. The endpoint's content type needs to be multipart/form-data. <br>

It is advised to use POSTMAN to upload the images to the url but you can also use curl to upload files the following way: <br>
```curl -X POST "http://localhost:8000/api/v1/upload/" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@test.png;type=image/jpeg"```
