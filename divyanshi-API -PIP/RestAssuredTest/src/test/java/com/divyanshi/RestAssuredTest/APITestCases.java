package com.divyanshi.RestAssuredTest;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.apache.poi.ss.usermodel.*;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;


import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import static io.restassured.RestAssured.given;
import static io.restassured.module.jsv.JsonSchemaValidator.matchesJsonSchema;

public class APITestCases {

    private static final String BASE_URL = "https://fakestoreapi.com";
    private static final String PRODUCTS_ENDPOINT = "/products";

    private Workbook workbook;

    @BeforeClass
    public void setUp() throws IOException {
        FileInputStream excelFile = new FileInputStream(new File("C:\\Users\\divyanshi7\\Desktop\\divyanshi2.xlsx"));
        workbook = WorkbookFactory.create(excelFile);
    }

    @Test
    public void testCreateProductsFromExcel() {
        Sheet sheet = workbook.getSheetAt(0); // Assuming the data is in the first sheet
        for (int rowIndex = 1; rowIndex <= sheet.getLastRowNum(); rowIndex++) {
            Row row = sheet.getRow(rowIndex);

            Cell titleCell = row.getCell(0);
            String title = titleCell != null ? titleCell.getStringCellValue() : "";

            Cell priceCell = row.getCell(1);
            double price = priceCell != null ? priceCell.getNumericCellValue() : 0.0;

            Cell descriptionCell = row.getCell(2);
            String description = descriptionCell != null ? descriptionCell.getStringCellValue() : "";

            Cell imageCell = row.getCell(3);
            String image = imageCell != null ? imageCell.getStringCellValue() : "";

            Cell categoryCell = row.getCell(4);
            String category = categoryCell != null ? categoryCell.getStringCellValue() : "";

            String requestPayload = String.format("{\"title\": \"%s\",\"price\": %.2f,\"description\": \"%s\",\"image\": \"%s\",\"category\": \"%s\"}",
                    title, price, description, image, category);

            System.out.println("Sending request payload: " + requestPayload);

            // Send POST request and validate response
            Response response = given()
                    .baseUri(BASE_URL)
                    .basePath(PRODUCTS_ENDPOINT)
                    .header("Content-Type", "application/json")
                    .body(requestPayload)
                    .when()
                    .post();

            // Validate status code
            int expectedStatusCode = 200;
            int actualStatusCode = response.getStatusCode();
            Assert.assertEquals(actualStatusCode, expectedStatusCode,
                    "Expected status code: " + expectedStatusCode + ", but found: " + actualStatusCode);

            System.out.println("Status code validated: " + actualStatusCode);

            // Validate content-type header
            String expectedContentType = "application/json; charset=utf-8";
            String actualContentType = response.getHeader("Content-Type");
            Assert.assertEquals(actualContentType, expectedContentType,
                    "Expected content type: " + expectedContentType + ", but found: " + actualContentType);

            System.out.println("Content type validated: " + actualContentType);

            // Validate JSON Schema for response payload
            String schema = "{\"$schema\":\"http://json-schema.org/draft-04/schema#\",\"type\":\"object\",\"properties\":{\"title\":{\"type\":\"string\"},\"price\":{\"type\":\"number\"},\"description\":{\"type\":\"string\"},\"image\":{\"type\":\"string\"},\"category\":{\"type\":\"string\"}},\"required\":[\"title\",\"price\",\"description\",\"image\",\"category\"]}";
            response.then().assertThat().body(matchesJsonSchema(schema));

            System.out.println("JSON Schema validated");

            // Additional assertions or verifications can be added here based on the response content
        }
    }
}
