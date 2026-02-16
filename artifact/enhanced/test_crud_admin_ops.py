from enhanced.crud_module_enhanced import CRUD
import os

def main():
    # Connects the same way original dashboard does
    mongo_uri = os.getenv("MONGO_URI")
    if mongo_uri:
        db = CRUD(uri=mongo_uri, db_name="aac", collection="animals")
    else:
        db = CRUD(host="localhost", port=27017, db_name="aac", collection="animals")

    # 1) CREATE (safe marker document)
    test_doc = {
        "name": "CS499_TEST_ANIMAL",
        "animal_type": "Dog",
        "breed": "Test Breed",
        "cs499_marker": True
    }
    inserted_id = db.create(test_doc)
    print("CREATE ok, id:", inserted_id)

    # 2) READ (verify it exists)
    results = db.read({"cs499_marker": True, "name": "CS499_TEST_ANIMAL"}, projection={"_id": 0})
    print("READ ok, found:", len(results))

    # 3) UPDATE (change breed)
    matched, modified = db.update(
        {"cs499_marker": True, "name": "CS499_TEST_ANIMAL"},
        {"breed": "Updated Test Breed"}
    )
    print("UPDATE ok, matched:", matched, "modified:", modified)

    # 4) DELETE (clean up)
    deleted = db.delete({"cs499_marker": True, "name": "CS499_TEST_ANIMAL"}, many=True)
    print("DELETE ok, deleted:", deleted)

if __name__ == "__main__":
    main()
