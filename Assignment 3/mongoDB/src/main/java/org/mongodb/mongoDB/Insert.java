package org.mongodb.mongoDB;

import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import org.bson.Document;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;

public class Insert 
{
	@SuppressWarnings("resource")
	public static void main( String[] args )
	{
		MongoClientURI connectionString = new MongoClientURI("mongodb://127.0.0.1:27017");
		MongoDatabase database = new MongoClient(connectionString).getDatabase("admin");
		MongoCollection<Document> collection = database.getCollection("Library");
		Logger mongoLogger = Logger.getLogger("org.mongodb.driver");
		mongoLogger.setLevel(Level.SEVERE); 
		try 
		{
		String currentFolder = System.getProperty("user.dir");
		PDDocument pdf_book = PDDocument.load(new File(currentFolder + "/Harry Potter.pdf"));
		String text = "";
		if (!pdf_book.isEncrypted()) 
		{
			PDFTextStripper stripper = new PDFTextStripper();
			text = stripper.getText(pdf_book);
		}
		pdf_book.close();				
		Document document = new Document()
				.append("Book name", "Harry Potter")
				.append("Author", "JK Rollwing")
				.append("Editor", "Folio Junior")
				.append("Edit year", 2004)
				.append("Book", text);
		collection.insertOne(document);
		}
		catch (IOException ex) 
		{
			System.out.println(ex);
		}
	}
}

