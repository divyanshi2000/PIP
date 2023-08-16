package com.divyanshi.RestAssuredTest;

import io.restassured.RestAssured;
import io.restassured.module.jsv.JsonSchemaValidator;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import java.util.List;
import java.util.Map;

public class CartsApiTest {

    @BeforeClass
    public void setUp() {
        RestAssured.baseURI = "https://fakestoreapi.com";
    }

    @Test
    public void testResponseSchema() {
        Response response = RestAssured.given().log().all().get("/carts").then().log().all().extract().response();

        // Log response details
        logResponse(response);

        // Validate status code
        response.then().assertThat().statusCode(200);

        // Validate content type
        response.then().assertThat().contentType("application/json; charset=utf-8");

        boolean isSchemaValid = response.then().extract().asString().matches("carts-schema.json");
        if (isSchemaValid) {
            System.out.println("Response follows the schema");
        } else {
            System.out.println("Response is not following the schema");
        }
        response.then().assertThat().body(JsonSchemaValidator.matchesJsonSchemaInClasspath("carts-schema.json"));

        // Validate JSON schema

    }

    @Test
    public void testProductsFields() {
        Response response = RestAssured.given().log().all().get("/carts").then().log().all().extract().response();

        // Log response details
        logResponse(response);

        // Validate status code
        response.then().assertThat().statusCode(200);

        // Validate content type
        response.then().assertThat().contentType("application/json; charset=utf-8");

        List<Map<String, Object>> carts = response.jsonPath().getList("");

        for (Map<String, Object> cart : carts) {
            List<Map<String, Object>> products = (List<Map<String, Object>>) cart.get("products");
            if (!products.isEmpty()) {
                for (Map<String, Object> product : products) {
                    Assert.assertNotNull(product.get("productId"), "productId is null");
                    Assert.assertNotNull(product.get("quantity"), "quantity is null");
                }
                System.out.println("At least one product is there and fields are not null");
            }
            else {
                System.out.println("Found error: No products or fields are null");
            }
        }
    }

    // Helper method to log response details
    private void logResponse(Response response) {
        System.out.println("Response Status Code: " + response.getStatusCode());
//        System.out.println("Response Body: " + response.getBody().asString());
    }
}
