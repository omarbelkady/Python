## GraphQL
- Query Language

#### REST & SOAP
- Technologies used to allow different services to communicate together


##### Example Of HTTP verbs to obtain resources aka 727225 resources
- http GET /posts
- http PUT /posts/1
- http DELETE /posts/1
- http POST /posts/1/comments


##### Gmail And Google Maps
- Such applications used this technology to perform certain tasks without a page refresh

##### FB used it too
- The ability to have >1,000,000,000 users on their platform without affecting the bandwidth

##### Iphone(Best Phone Ever) launch in 2007
- Brought the introduction of hybrid apps(web and mobile) and the concept of BORA


##### APIs
- Used to allow for communication to take place between one backend or multiple backends

##### Beauty of A QL
- uses a single document to obtain the data you requested
- responds in JSON format

#### How To Create A Query in GraphQL
```graphql
query ListThePascalCategories{
	pascalcategories{
		pascalname{
		}
	}
}
```

### How To Create A Query With Data Passed In Thanks to Mutation format: name operationType
```graphql
mutation EditPascCategory($id: ID!){
	editCategory(id: $id, title: "..."){
		category{
			title
			...
		}
	}
}
```

### How To Subscribe to An Event In The Backend
```graphql
subscription OnCategoryUpdate($id: ID!){
	onCategoryUpdate(id: $id){
		category{
			title
		}
	}
}
```

### How the API Gateway works in GraphQL
```
One API Gateway that talks to multiple graphql apis and then it does the API
calls for me.
For example, I have user microservices and a post microservices, and I make a 
request for the user the post microservices will query both. 
On the FE however, this is transparent. If you work with FE there are clients
who deal with GraphQL 
```

### GraphQL does the three steps on the go without having to worry
- data fetching
- data normalization
- storage in a temporary store

### Now All I have to do is:
- display on the FE


### Data Class
- Built in class Decorator that is a data container aka a class that only holds data
```python
@dataclass
class CharacterisOfPascFB:
	favLang: string
	favOS: int
	likesToWriteLLC: bool
```

### How To Pass Data to GraphQL in Python thanks to Decorator
```python
@ll.type
class Query:
	@ll.field
	def categories(self, info, max_categories: typing.Optional[int] = None) -> typing.List[Categories]
		max_categories = max_categories or 10
	
		return db.fetch_categories(limit=max_categories)
```
### GraphQL supports:
- Asynchronous Tasks
- Unions
- Queries
- Mutations
- Subscriptions
- Debug Server
